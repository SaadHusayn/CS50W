from django import forms
from .models import Post, User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['postContent', ]
        widgets = {
            'postContent':forms.Textarea(attrs={'class':'form-control', 'rows':3, 'autofocus':True})
        }
        labels = {
            'postContent':'New Post'
        } 