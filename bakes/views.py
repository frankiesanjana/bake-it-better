from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Bake, Comment
from .forms import BakeForm, CommentForm


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
            starred = True

        return render(
            request,
            "bake-detail.html",
            {
                "bake": bake,
                "comments": comments,
                "commented": False,
                "starred": starred,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Bake.objects.filter(status=1)
        bake = get_object_or_404(queryset, slug=slug)
        comments = bake.comments.filter(approved=True).order_by('created_on')
        starred = False
        if bake.stars.filter(id=self.request.user.id).exists():
            starred = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.bake = bake
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "bake-detail.html",
            {
                "bake": bake,
                "comments": comments,
                "commented": True,
                "starred": starred,
                "comment_form": CommentForm()
            },
        )


class BakeStar(View):
    """
    Creates the view code to allow users to star bakes
    """
    def post(self, request, slug):
        bake = get_object_or_404(Bake, slug=slug)

        if bake.stars.filter(id=request.user.id).exists():
            bake.stars.remove(request.user)
        else:
            bake.stars.add(request.user)

        return HttpResponseRedirect(reverse('bake-detail', args=[slug]))


class MyStarredBakes(LoginRequiredMixin, generic.ListView):
    """
    Creates the view code to allow users to view 
    all the bakes that they have starred
    """
    model = Bake
    queryset = Bake.objects.filter(status=1).order_by('-created_on')
    template_name = 'my-starred-bakes.html'
    paginate_by = 8


class AddBake(LoginRequiredMixin, generic.CreateView):
    """
    Creates the view code to allow users to add a new bake
    """
    model = Bake
    form_class = BakeForm
    template_name = 'add-bake.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateBake(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """
    Creates the view code to allow users to edit a bake
    that they have previously added
    """
    model = Bake
    form_class = BakeForm
    template_name = 'edit-bake.html'
    
    def test_func(self):
        """
        Prevents users from editing bakes written by other users
        """
        return Bake.author == self.request.user


class DeleteBake(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    Creates the view code to allow users to delete a bake
    that they have previously added
    """
    model = Bake
    template_name = 'delete-bake.html'
    success_url = '/home'

    def test_func(self):
        """
        Prevents users from deleting bakes written by other users
        """
        return Bake.author == self.request.user