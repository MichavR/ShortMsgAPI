"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from ShortMsg import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', views.MessagesViewSet.as_view({'get': 'list'}), name='msg_viewset'),
    path('view_msg/<int:pk>', views.MessageView.as_view(), name='view_msg'),
    path('create_msg/', views.CreateMessage.as_view(), name='create_msg'),
    path('delete_msg/<int:pk>', views.DeleteMessage.as_view(), name='delete_msg'),
    path('edit_msg/<int:pk>', views.EditMessage.as_view(), name='edit_msg'),
]
