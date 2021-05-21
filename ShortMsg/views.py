import datetime
import django.db.utils
from django.http import Http404
from ShortMsg.models import Message
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ShortMsg.serializers import MessageSerializer


class Obj:
    def get_object(self, pk):
        try:
            return Message.objects.get(pk=pk)
        except Message.DoesNotExist:
            raise Http404


class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-datetime')
    serializer_class = MessageSerializer


class MessageView(APIView):
    def get(self, request, pk):
        try:
            message = Obj.get_object(request, pk)
            message.views_count = message.views_count+1
            message.save()
            serializer = MessageSerializer(message, context={"request": request})
            return Response(serializer.data)
        except django.db.utils.ProgrammingError:
            raise Http404


class CreateMessage(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            serializer = MessageSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class DeleteMessage(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        message = Obj.get_object(request, pk)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EditMessage(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        message = Obj.get_object(request, pk)
        message.views_count = 0
        message.datetime = datetime.datetime.now()
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
