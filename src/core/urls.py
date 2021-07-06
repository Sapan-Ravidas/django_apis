from django.urls import path
from .views import PostView, PostCreateView, PostListCreateView

urlpatterns = [
    path('', PostView.as_view(), name="test-view"),
    path('create/', PostCreateView.as_view(), name='create-view'),
    path('list-create/', PostListCreateView.as_view(), name='list-create-view'),
]