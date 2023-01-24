from .models import Bake, Comment
from django import forms


class BakeForm(forms.ModelForm):
    """
    Creates the form to add and edit bakes
    """
    def __init__(self, *args, **kwargs):
        super(BakeForm, self).__init__(*args, **kwargs)
   
    class Meta:
      """
      Displays fields from recipe model
      """
      model = Bake
      fields = [
         'title',
         'description',
         'difficulty',
         'equipment',
         'ingredients',
         'method',
         'featured_image',
         'status'
      ]


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