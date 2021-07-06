from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# APIView is one of the warppers that allow to create a api view that accepts cretain request methods 
# either get request or a post request, and all the otehr types of methods

# instead of creating functions, we create a class. Because APIView is something which inherit in
# our own classes

class TestView(APIView):
    # when someone set the get rewuest
    def get(self, request, *args, **kwargs):
        data = {
            'name' : 'sapan',
            'age' : 23,
            }
        
        return Response(data)
        
        