from django.urls import path
from .views import PostList, PostDetail, HelloWorldView

urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("hello-world/", HelloWorldView.as_view(), name="hello_world"),
]