from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.full_post, name='full_post'),
	path('post/new/', views.post_new, name='post_new'),
]