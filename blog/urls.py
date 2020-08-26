from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(PostListView.as_view()), name='home-blog'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='about-blog'),
]

#<app>/<model>_<viewtype>.html