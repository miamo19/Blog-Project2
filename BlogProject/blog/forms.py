#From Project
from .models import Comment

#From Django
from django import forms


class CommentForm(forms.ModelForm):
    """ description: This class create a form to be filled before commenting on a specific post """
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
