
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.views import View

from .models import Post


class PostList(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"


class PostDetail(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class HelloWorldView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello World")
