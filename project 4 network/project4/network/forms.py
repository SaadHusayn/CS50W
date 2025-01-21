from django import forms
from .models import Post, User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['postContent', ]
        widget = {
            'content':forms.Textarea(attrs={'class':'form-control', 'rows':3})
        }
        labels = {
            'content':'New Post'
        }