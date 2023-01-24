from .models import Bake, Comment
from django import forms


class BakeForm(forms.ModelForm):
   """
       Creates the form to add and edit bakes
   """
   class Meta:
      """
         Displays fields from recipe model
      """
      model = Bake
      fields = "__all__"

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