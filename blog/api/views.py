
from blog.models import Post
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import Http404 
from .serializer import PostSerializer


@api_view(["GET", "POST"])
def api_home_view(request):
    if request.method =='GET':
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


@api_view(["GET"])
def api_detail_view(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response("Post not valid")

    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)