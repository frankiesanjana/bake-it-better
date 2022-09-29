from django.shortcuts import render
from django.views import generic
from .models import Bake

class BakeList(generic.ListView):
    """
    Creates the view code to display bakes
    """
    model = Bake
    queryset = Bake.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8
