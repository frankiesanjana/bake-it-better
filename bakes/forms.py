from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Bake, Comment, BestFor


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
         'featured_image'
        ]
        widgets = {
         'description': SummernoteWidget(),
         'equipment': SummernoteWidget(),
         'ingredients': SummernoteWidget(),
         'method': SummernoteWidget(),
        }


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


class BestForForm(forms.ModelForm):
    """
    Creates the form to add Best For bakes
    """
    class Meta:
        """
        Defines the model and form fields
        """
        model = BestFor
        fields = ('best_for',)
