from django.urls import path
from .views import UserPostListView, MyPost
from . import views


app_name = 'web'



urlpatterns = [
    path('<str:username>/user/', UserPostListView.as_view(), name="user_posts"),
    path('my_post/', MyPost.as_view(), name="my_posts"),
    path('<int:pk>/post_edit/', views.post_edit, name="post_edit"),
    path('<int:pk>/post_delete/', views.post_delete, name="post_delete"),
    path('<int:pk>/favourite_post/', views.favourite_post, name="favourite_post"),
    path('<int:pk>/<slug:slug>/', views.post_detail, name="post_detail"),
    path('post_create/', views.post_create, name="post_create"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('favourites/', views.post_favourite_list, name="post_favourite_list"),

]
