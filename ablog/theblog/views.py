from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import PostApi
from .serializers import PostAPISerializers

# def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class PostAPIView(viewsets.ViewSet):
    def list(self, request):
        post_apies = PostApi.object.all()
        serializer = PostAPISerializers(post_apies, many=True)
        return Response(serializer.data)
        
    def create(self, request):
        serializer = PostAPISerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class PostAPIViewSet(viewsets.ViewSet): 
    def retrieve(self, pk=None):
        post_api = PostApi.object.get(id=pk)
        serializer = PostAPISerializers(post_api)
        return Response(serializer.data)
        
    def update(self, request, pk=None):
        post_api = PostApi.object.get(id=pk)
        serializer = PostAPISerializers(instance=post_api, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)    
        
    def destroy(self, request, pk=None):
        post_api = PostApi.object.get(id=pk)
        post_api.delete
        return Response(status=status.HTTP_204_NO_CONTENT)
