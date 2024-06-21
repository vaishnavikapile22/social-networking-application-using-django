Social Network API

This is a social networking API built with Django Rest Framework. The API provides functionalities for user signup, login, searching users, sending/accepting/rejecting friend requests, listing friends, and viewing pending friend requests.

Features

User Signup
User Login
Search Users by Email or Name
Send Friend Request
Accept/Reject Friend Request
List Friends
List Pending Friend Requests
Rate limiting on sending friend requests

Installation

git clone https://github.com/vaishnavikapile22/social-networking-application-using-django.git

cd social-networking-application-using-django

create vartiual env

pip install django

pip install djangorestframework

pip install djangorestframework-simplejwt

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

API Endpoints
User Signup
URL: /api/signup/
Method: POST
{
    "email": "mina2@gmail.com",
    "username": "mina",
    "password": "123",
    "first_name": "mina",
    "last_name": "pawar"
}

OUTPUT

![Screenshot (95)](https://github.com/vaishnavikapile22/social-networking-application-using-django/assets/149785862/63108580-254e-4fd6-92d8-e8f2ef8d468d)


{
    "user": {
        "id": 8,
        "email": "mina2@gmail.com",
        "username": "mina",
        "first_name": "mina",
        "last_name": "pawar"
    },
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxOTA0OTUzMywiaWF0IjoxNzE4OTYzMTMzLCJqdGkiOiJkY2MxZDMxMmEyYzU0MmEyODAzNDg5ZDRhZmYwNTJjNSIsInVzZXJfaWQiOjh9.UJEzz637G8bDG-tTroLQqweo0z1eD-_aeo48ZYlQyds",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4OTYzNDMzLCJpYXQiOjE3MTg5NjMxMzMsImp0aSI6IjIzNzA1N2ViOGYwOTQzNjNiY2VkMTIzMWU4MGE4MWM4IiwidXNlcl9pZCI6OH0.5g-ePjGmVwZRXagSSwBMDrAI-VPW-1xYlCkshZQwruw"
}

User Login
URL: /api/login/
Method: POST
Request:
{
    "email":"kapile@22gmail.com",
    "password": "1234"
}

OUTPUT

{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxOTA1MDAyMCwiaWF0IjoxNzE4OTYzNjIwLCJqdGkiOiIyODcwYmVjNTk3MzQ0MzE3OWE4ODViNzRiYTYyOWNkYyIsInVzZXJfaWQiOjd9.pxFNDmXaPMt1WoXYMKt0Ylpa8T4d6hjfKbgCfQWJxY0",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4OTYzOTIwLCJpYXQiOjE3MTg5NjM2MjAsImp0aSI6IjZlZmRiYjU1Y2MyZTQ2MWE4ZWY2MTA5N2RjNmU2NzlkIiwidXNlcl9pZCI6N30.Fb-OAw5nZnh7cLdipJAXOb3_PpPVaikRv6SaGDnORT0"
}

![Screenshot (96)](https://github.com/vaishnavikapile22/social-networking-application-using-django/assets/149785862/0101ada9-912a-476d-8849-9903e0332a78)


Search Users

Search Users
URL: [/api/search/](http://127.0.0.1:8000/api/search/?q=mi)
Method: GET

OUTPUT

![Screenshot (97)](https://github.com/vaishnavikapile22/social-networking-application-using-django/assets/149785862/16ee200a-04b1-427d-9da7-a83233d6a4cd)



Send Friend Request

URL: /api/friend-request/send/
Method: POST
Request:
{
    "to_user_id": 7
}

OUTPUT

![Screenshot (99)](https://github.com/vaishnavikapile22/social-networking-application-using-django/assets/149785862/fb91a1f1-dce2-42f4-84a5-45d62b17bfa8)


Accept/Reject Friend Request

URL: /api/friend-request/action/
Method: POST
Request:
{
    "request_id": 5,
    "action":"accept"
}

![Screenshot (100)](https://github.com/vaishnavikapile22/social-networking-application-using-django/assets/149785862/3c7e1341-271f-46a0-81f0-f90b2b6202d1)




URL: /api/friend-request/pending/
Method: GET

URL:http://127.0.0.1:8000/api/friends
Method :GET
![Screenshot (101)](https://github.com/vaishnavikapile22/social-networking-application-using-django/assets/149785862/fe702f77-296c-4739-a8f6-89582af1d618)

![alt text](<Screenshot (101).png>)




