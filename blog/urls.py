from django.urls import path
from .views import (
    HomeView,
    AboutView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    )

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('user/<str:username>/',UserPostListView.as_view(),name='user_posts'),
    path('about',AboutView.as_view(),name='about'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='detail'),
    path('post/new/',PostCreateView.as_view(),name='post_create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post_update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post_delete'),
]

