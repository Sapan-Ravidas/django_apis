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