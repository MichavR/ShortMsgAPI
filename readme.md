# Short Message API

## Table of contents
* [Overview](#overview)
* [Installation](#installation)
* [Setup](#setup)
* [Endpoints](#endpoints)
   * [Authentication](#authentication)
   * [Message viewset](#message-viewset)
   * [Message details](#message-details)
   * [Create message](#create-message)
   * [Edit message](#edit-message)
   * [Delete message](#delete-message)

<a name="overview"></a>
## Overview 
Short Message API app is a backend REST application written in Python (Django & Django REST frameworks). It allows user to store and share short messages/memos (maximum of 160 characters).

Message object contains: 
- "text" - the message's content
- "datetime" - automatically added date and time of message creation/last edition
- "author" - contains id of user who created/edited message
- "views_count" - message's views counter

<a name="installation"></a>
## Installation

For Linux (Windows users should use 'set' command instead of 'export'):
- set the `SECRET_KEY` variable:
  ```bash 
  export SECRET_KEY='enter_your_secret_key_here'
  ```  

- set database credentials:
  ```bash
  export DATABASE_URL='enter_your_database_url_here'
  ``` 

  or setup own database engine, e.g.:
  ```bash
  export DATABASES='{default: {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3",}}'
  ```
  **>>>Remember to set up virtual environment<<<**\
  \
  Install required packages:
  ```bash
  pip install -r requirements.txt
  ```

<a name="setup"></a>
## Setup
### Make database migration
From app's directory run:
```bash
python manage.py migrate
```

### Run application
```bash
python manage.py runserver
```
Locally app is accessible at http://127.0.0.1:8000/ by default.

### Testing
Set `DEBUG` mode:\
ON: `export DEBUG='True'`\
or\
OFF:`export DEBUG='False'`
  
For testing purposes use these credentials:\
   username: test\
   password: Testing.123

<a name="endpoints"></a>
## Endpoints

<a name="authentication"></a>
### Authentication:
   Authentication is required for creating, editing and deleting messages.
   
   Application uses token authentication method. 
   To authenticate user, send POST request to: 
   'https://short-msg-api.herokuapp.com/api-token-auth/'
   
   The request must pass user credentials (username and password) in request's BODY (JSON):
   ```JSON
   {"username": "xxx", "password": "yyy"}
   ```
   
   Response body is the token associated with particular user:
   
   ```json
   {
    "token": "your_token_here"
   }
   ```
   
   Every request to views responsible for message creation, edition, deletion must contain token in its header, e.g. KEY: Authentication, VALUE: Token *your_token_here*

<a name="message-viewset"></a>
### Message Viewset:
  url: https://short-msg-api.herokuapp.com/ \
  request: GET\
  no authentication needed\
  returns viewset containing list of all created messages ordered by datetime of creation/edition
  
  Response example:
  ```json
  [
    {
        "id": 2,
        "text": "testing2",
        "datetime": "2021-05-21T19:49:11.458395Z",
        "author": 2,
        "views_count": 0
    },
    {
        "id": 1,
        "text": "testing1",
        "datetime": "2021-05-21T19:48:58.528654Z",
        "author": 2,
        "views_count": 0
    }
   ]
  ```

<a name="create-message"></a>
### Create Message:
  url: https://short-msg-api.herokuapp.com/create_msg/ \
  request: POST\
  authentication needed\
  allows to create new message\
  request BODY must contain JSON "text" value, e.g.: `{"text": "example"}` other values as "datetime", "author", "view_count" will be provided automatically; "text" value must contain at least 1 character, otherwise it will not be saved
  
  Request example:\
  cURL:
  ```cURL
  curl --location --request POST 'https://short-msg-api.herokuapp.com/create_msg/' \
   --header 'Authorization: Token your_token_here' \
   --header 'Content-Type: application/json' \
   --data-raw '{"text": "test2"}'
  ```
  or\
  Python - Requests:
  ```python
  import requests

   url = "https://short-msg-api.herokuapp.com/create_msg/"

   payload = "{\"text\": \"test2\"}"
   headers = {
     'Authorization': 'Token your_token_here',
     'Content-Type': 'application/json'
   }

   response = requests.request("POST", url, headers=headers, data=payload)

   print(response.text)
  ```
  Response example:
  ```JSON
  {
    "id": 3,
    "text": "test2",
    "datetime": "2021-08-10T20:26:55.720881Z",
    "author": 2,
    "views_count": 0
   }
  ```
 <a name="message-details"></a> 
 ### Message Details:
  url: https://short-msg-api.herokuapp.com/view_msg/{id} \
  request: GET\
  no authentication needed\
  allows to view single message details as its text content, datetime of creation, author and views count. Id (int) of demanded message must be provided in url. Every request increases views count by 1 for particular message
  
  Request example:\
  cURL:
  ```cURL
   curl --location --request GET 'https://short-msg-api.herokuapp.com/view_msg/3'
  ```
  or\
  Python - Requests:
  ```python
   import requests

   url = "https://short-msg-api.herokuapp.com/view_msg/3"

   payload = {}
   headers = {}

   response = requests.request("GET", url, headers=headers, data=payload)

   print(response.text)
  ```
  
  Response example:
  ```JSON
  {
    "id": 3,
    "text": "test2",
    "datetime": "2021-08-10T20:26:55.720881Z",
    "author": 2,
    "views_count": 2
   }
  ```
<a name="edit-message"></a>  
### Edit Message:
  url: https://short-msg-api.herokuapp.com/edit_msg/{id} \
  request: PUT\
  authentication needed\
  allows to edit particular message - id (int) of message must be provided in url; edit resets datetime to current and views counter to 0
  
  Request example:\
  cURL:
  ```cURL
   curl --location --request PUT 'https://short-msg-api.herokuapp.com/edit_msg/3' \
   --header 'Authorization: Token your_token_here' \
   --header 'Content-Type: application/json' \
   --data-raw '{"text": "edited_text"}'
  ```
  or\
  Python - Requests:
  ```python
   import requests

   url = "https://short-msg-api.herokuapp.com/edit_msg/3"

   payload="{\"text\": \"edited_text\"}"
   headers = {
     'Authorization': 'Token your_token_here',
     'Content-Type': 'application/json'
   }

   response = requests.request("PUT", url, headers=headers, data=payload)

   print(response.text)

  ```
  
  Response example:
  ```JSON
   {
    "id": 3,
    "text": "edited_text",
    "datetime": "2021-08-10T20:43:01.731873Z",
    "author": 2,
    "views_count": 0
   }
  ```

<a name="delete-message"></a>
### Delete Message:
  url: https://short-msg-api.herokuapp.com/delete_msg/{id} \
  request: DELETE\
  authentication needed\
  allows to delete single message with id (int) provided in url
  
  Request example:\
  cURL:
  ```cURL
   curl --location --request DELETE 'https://short-msg-api.herokuapp.com/delete_msg/3' \
   --header 'Authorization: Token your_token_here'
  ```
  or\
  Python - Requests:
  ```python
   import requests

   url = "https://short-msg-api.herokuapp.com/delete_msg/3"

   payload={}
   headers = {
     'Authorization': 'Token your_token_here'
   }

   response = requests.request("DELETE", url, headers=headers, data=payload)

   print(response.text)

  ```


