Short Message API

0. About: Short Message API allows user to store short messages/memos (maximum of 160 characters).

Message object contains: 
- "text" - the message's content
- "datetime" - automatically added date and time of message creation/last edition
- "author" - contains id of user who created/edited message
- "views_count" - message's views counter

1. Authentication
   Authentication is required for creating, editing and deleting messages.
   
   Application uses token authentication method. 
   To authenticate user, send POST request to: 
   'https://short-msg-api.herokuapp.com/api-token-auth/'
   
   The request must pass user credentials (username and password) in request's BODY:
   {"username": "xxx", "password": "yyy"}
   
   Response body is the token associated with particular user. Every request to views responsible for message creation, 
   edition, deletion must contain token in its header, e.g. KEY: Authentication, VALUE: Token <token>
   
2. Endpoints
- Message Viewset:
  url: https://short-msg-api.herokuapp.com/
  request: GET
  no authentication needed
  returns viewset containing list of all created messages ordered by datetime of creation/edition
  
- Create Message:
  url: https://short-msg-api.herokuapp.com/create_msg/
  request: POST
  authentication needed
  allows to create new message
  request BODY must contain "text" value, e.g.: {"text": "example"} other values as "datetime", "author", "view_count" 
  will be provided automatically; "text" value must contain at least 1 character, otherwise it will not be saved
  
- Message Details
  url: https://short-msg-api.herokuapp.com/view_msg/<id>
  request: GET
  no authentication needed
  allows to view single message details as its text content, datetime of creation, author and views count. Id (int) of 
  demanded message must be provided in url. Every request increases views count by 1 for particular message
  
- Edit Message:
  url: https://short-msg-api.herokuapp.com/edit_msg/<id>
  request: PUT
  authentication needed
  allows to edit particular message - id (int) of message must be provided in url ; edit resets datetime to current and 
  views counter to 0
  
- Delete Message:
  url: https://short-msg-api.herokuapp.com/delete_msg/<id>
  request: DELETE
  authentication needed
  allows to delete single message with id (int) provided in url

3. Testing
For testing purposes use these credentials:
   username: test
   password: Testing.123
