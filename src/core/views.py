from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import PostSerializer
from .models import Post

# authentications
from rest_framework.permissions import IsAuthenticated

# APIView is one of the warppers that allow to create a api view that accepts cretain request methods 
# either get request or a post request, and all the otehr types of methods

# instead of creating functions, we create a class. Because APIView is something which inherit in
# our own classes

class TestView(APIView):
    permission_classes = (IsAuthenticated,)
    
    # when someone set the get rewuest
    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        # serializer = PostSerializer(queryset, many=True)
        post = queryset.first()
        serializer = PostSerializer(post)
        return Response(serializer.data)
        
    
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
# Basically we want to demonsttarte how to use, a serializer in two ways

# 1. When we recieve datas
# for example in POST request we receive some data in that request, we need to make sure that the format of 
# data matches with the serializer
# thats exactly like how form works


