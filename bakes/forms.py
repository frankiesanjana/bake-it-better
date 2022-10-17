from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
       Creates the form to add and edit comments
    """
    class Meta:
       """
       Defines the model and form fields
       """
       model = Comment
       fields = ('body',)