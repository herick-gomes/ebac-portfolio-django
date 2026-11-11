
from django.views.generic import ListView, DetailView
from .models import Post
from django.http import HttpResponse
from django.views import View


class PostList(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"


class PostDetail(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


class HelloWorldView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello World")
