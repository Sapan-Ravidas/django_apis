# What is API ?

Application Programming Interface.

A set of functions and procedures allowing the creation of applications that access the features or data of an operating system, application, or other service.

An application programming interface is a connection between computers or between computer programs. It is a type of software interface, offering a service to other pieces of software. A document or standard that describes how to build such a connection or interface is called an API specification.

## Why use API ?

May you have an application that you like to share with others, like people to integrate with it and use in their source. Or just you have multiple service that need to connect with one central service.

- API only provide data that you want to renderm typically in json format.


## Project pprogressiion

- Create a django project with name ```django_api```
- **djanfo_api**
    - create a app within the project with name ```core```
        - inside the views file

            we want to return only the data which is json payload

            ```from django.http import JsonResponse```
        
        - link views to url, and add these urlpatterns to main prohject url

        - until now, if you want to make sure that your api is working 
        - open terrminal and type ```curl <local-host-url>``` 
            ```
            $ curl http://127.0.0.1:8000/
            ```

## DjangoRestFramework

It allows you to build an api in lot easier and quicker, that you cant do in just normal djando

https://www.django-rest-framework.org/

```
$ pip install djangorestframework
```

add restframework in your installed-apps list inside main-project-settings file 

The views in core
```
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    # when someone set the get rewuest
    def get(self, request, *args, **kwargs):
        data = {
            'name' : 'sapan',
            'age' : 23,
            }
        
        return Response(data)
```

Add these views in app urls by
```
from django.urls import path
from .views import TestView

urlpatterns = [
    path('', TestView.as_view(), name="test-view"),
]
```

Add the app url to main-project url -> this will same 

# 01.

Typically we use django models to represt the data that we want how to store in our database. So, there be some way that we can return the data in the database using the django rest_framework, that means somehow we need to get it from our models.

Django rest_framework uses ```Serializer``` to do this. ```Serializer``` is basically a structre or representation of model or form and represent the data that you want to return in a json format or accept a json format. So we use those ```Serializer``` to transform our model to json.

- create a file ```serializer.py``` in core app.

```
from rest_framework import serializers
from .models import Post

class PostSerial(serializer.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'description')
```

So basically this serializer represent the transformation between a Post model into a json payload that conatins 'title' and 'description' fields on that model

the ```model.py``` file

```
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __repr__(self):
        return f"<Post(title='self.title')>"

```

Now we can this serializer in our views

- To test apis very easily we use postman

https://www.postman.com/

&nbsp;

# 02. Authentications

rest_framework.permisssions

- Allowany -> allows anyone to make a request to the end point
- IsAdminuser
- IsAuthenticated
- IsAuthenticatedOrReadOnly

To user TokenAuthentication we need to add ```rest_framework.authtoken``` in our installed app list in settings.py file

- to clear all in the database 

    run 
    ```
    $ python manage.py flush
    ```

- now create a new superuser.

- one very easy way to create a token for our admin user is just by 
    ```
    $ python manage.py drf_create_token <superusername>
    ```

- for token authentication we'll user ```django_rest_auth```
```
$ pip install django-rest-auth
```
and add to our app list
