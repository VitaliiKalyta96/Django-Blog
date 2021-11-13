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
        products = Product.object.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
        
    def create(self, request):
        serializer = ProductSerializer(data=requets.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class PostAPIViewSet(viewsets.ViewSet): 
    def retrieve(self, pk=None):
        product = Product.object.get(id=pk)
        serializer = ProductSerializer(products)
        return Response(serializer.data)
        
    def update(self, request):
        product = Product.object.get(id=pk)
        serializer = ProductSerializer(instatnce=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)    
        
    def destroy(self, request, pk=None):
        product = Product.object.get(id=pk)
        product.delete
        return Response(status=status.HTTP_204_NO_CONTENT)
