from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


# def home(request):
#     posts = Post.objects.all()

#     return posts


class Home(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/home.html"
    ordering = ["-date_posted"]   #to reverse the post by time created
# Create your views here.

class Detail(DetailView):
    model = Post
    template_name="blog/detail.html"
