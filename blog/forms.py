from django import forms

from .models import Post, Comment
from products.widgets import CustomFileInput


class PostForm(forms.ModelForm):
    # Posting code for the form 
    class Meta:
        model = Post
        fields = ['title', 'intro', 'image', 'body']

    image = forms.ImageField(
        label="Image",
        required=False,
        widget=CustomFileInput,
        )


class CommentForm(forms.ModelForm):
    # Form for the commenting aspect of the blog
    class Meta:
        model = Comment
        fields = ['body']