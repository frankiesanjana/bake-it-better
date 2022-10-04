from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Bake

class BakeList(generic.ListView):
    """
    Creates the view code to display a list of bakes
    """
    model = Bake
    queryset = Bake.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8


class BakeDetail(View):
    """
    Creates the view code to display individual bakes
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Bake.objects.filter(status=1)
        bake = get_object_or_404(queryset, slug=slug)
        comments = bake.comments.filter(approved=True).order_by('created_on')
        starred = False
        if bake.stars.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "bake-detail.html",
            {
                "bake": bake,
                "comments": comments,
                "starred": starred
            },
        )