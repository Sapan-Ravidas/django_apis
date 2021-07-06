from rest_framework import serializers
from .models import Post


# from django import forms

# # form
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title', 'description')


# serializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'description', 'owner')