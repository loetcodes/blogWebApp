from django import forms
from .models import BlogPost

class PostForm(forms.ModelForm):

	class Meta:
		""" Determines which model should be used to create the form
		"""
		model = BlogPost
		fields = ('title', 'text',)