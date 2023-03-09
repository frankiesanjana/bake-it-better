from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Bake, Comment, BestFor
from .forms import BakeForm, CommentForm, BestForForm


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
                "comment_form": CommentForm(),
                "best_for_form": BestForForm()
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
            messages.success(self.request, "Your comment has been added and is awaiting approval")
        else:
            comment_form = CommentForm()

        best_for_form = BestForForm(data=request.POST)

        if best_for_form.is_valid():
            best_for_bake = BestFor.objects.filter(user=request.user, best_for=request.POST['best_for']).first()
            
            try:
                best_for_bake.bake = bake
            except AttributeError:
                best_for_bake = best_for_form.save(commit=False)
                best_for_bake.user = request.user
                best_for_bake.bake = bake

            best_for_bake.save()
            messages.success(self.request, "This bake has been added to your Best For Bakes Plan!")

        else:
            best_for_form = BestForForm()


        return render(
            request,
            "bake-detail.html",
            {
                "bake": bake,
                "comments": comments,
                "commented": True,
                "starred": starred,
                "comment_form": CommentForm(),
                "best_for_form": BestForForm()
            },
        )


class BestForBakes(LoginRequiredMixin, generic.ListView):
    """
    Creates the view code to allow users to view 
    their saved Best For bakes
    """
    def get(self, request):
        # get all best for bakes from the signed-in user
        user_best_for_bakes = BestFor.objects.filter(user=request.user)

        # filter by occasion
        # if the occasion has a BF bake associated with it, add bake
        # if no BF bake exists, set occasion BF bake to none
        my_best_for_bakes = {}
        for each_category in BestFor.BEST_FOR_CHOICES:
            result_for_category = user_best_for_bakes.filter(best_for=each_category[0]).first() or None
            my_best_for_bakes[each_category[1]] = result_for_category
        
        return render(
            request,
            "best-for-bakes.html",
            {
                "my_best_for_bakes": my_best_for_bakes,
            },
        )


class BakeStar(View):
    """
    Creates the view code to allow signed-in users
    to star bakes
    """
    def post(self, request, slug):
        bake = get_object_or_404(Bake, slug=slug)

        if bake.stars.filter(id=request.user.id).exists():
            bake.stars.remove(request.user)
            messages.success(self.request, "Bake successfully unstarred")
        else:
            bake.stars.add(request.user)
            messages.success(self.request, "Bake successfully starred")

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


class AddBake(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """
    Creates the view code to allow users to add a new bake
    """
    model = Bake
    form_class = BakeForm
    template_name = 'add-bake.html'
    success_message = "%(title)s was created successfully"

    def get_success_message(self, cleaned_data):
        """
        Adds bake name into confirmation message
        """
        return self.success_message % dict(
            cleaned_data,
            title=self.object.title,
        )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateBake(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    """
    Creates the view code to allow users to edit a bake
    that they have previously added
    """
    model = Bake
    form_class = BakeForm
    template_name = 'edit-bake.html'
    success_message = "%(title)s was edited successfully"

    def get_success_message(self, cleaned_data):
        """
        Adds bake name into confirmation message
        """
        return self.success_message % dict(
            cleaned_data,
            title=self.object.title,
        )
    
    def test_func(self):
        """
        Prevents users from editing bakes written by other users
        except for the admin user, who is allowed to edit others' bakes
        """
        Bake = self.get_object()
        return Bake.author == self.request.user or self.request.user.is_superuser


class DeleteBake(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.DeleteView):
    """
    Creates the view code to allow users to delete a bake
    that they have previously added
    """
    model = Bake
    template_name = 'delete-bake.html'
    success_url = "/"
    success_message = "Bake %(title)s deleted successfully."

    def delete(self, request, *args, **kwargs):
        """
        Adds delete message via custom code (since DeleteView is not form-based)
        Code adapted from the following Stack Overflow article:
        https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown
        """
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(DeleteBake, self).delete(request, *args, **kwargs)

    def test_func(self):
        """
        Prevents users from deleting bakes written by other users
        except for the admin user, who is allowed to delete others' bakes
        """
        Bake = self.get_object()
        return Bake.author == self.request.user or self.request.user.is_superuser