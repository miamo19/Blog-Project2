#from Django
from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """ 
    name: CommentForm
    description: This class give a form to be fill before commenting on a specific post
    """
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
