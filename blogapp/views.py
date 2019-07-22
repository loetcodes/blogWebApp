from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import BlogPost
from .forms import PostForm

# Create your views here.

def post_list(request):
	posts = BlogPost.objects.filter(date_published__lte=timezone.now()).order_by('date_published')
	return render(request, 'blogapp/post_list.html', {'posts': posts})

def full_post(request, pk):
	post = get_object_or_404(BlogPost, pk=pk)
	return render(request, 'blogapp/full_post.html', {'post': post})

def post_new(request):
	form = PostForm()
	return render(request, 'blogapp/post_edit.html', {'form': form})