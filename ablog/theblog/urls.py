from django.urls import path, include
# from . import views
from .views import HomeView, ArticleDetailView, PostAPIView, PostAPIViewSet

urlpatterns = [
#     path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('post2/', PostAPIView.as_view({
        'get': 'list',
        'post': 'create'
        })),
    path('post2/<str:pk>', PostAPIViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
        })),
]
