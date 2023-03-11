"""
Imports external libraries for the program
"""
from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Bake(models.Model):
    """
       Defines the main model for bakes
    """
    LEVEL = [
        (1, 'easy'),
        (2, 'moderate'),
        (3, 'challenging'),
    ]

    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    difficulty = models.IntegerField(choices=LEVEL, default=1)
    equipment = models.TextField()
    ingredients = models.TextField()
    method = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=1)
    stars = models.ManyToManyField(User, related_name='bake_stars', blank=True)

    class Meta:
        """
        Orders the bakes by the order in which they were posted,
        most recent first
        """
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('bake-detail', kwargs={'slug': self.slug})

    def number_of_stars(self):
        """
        Shows how many users have starred the bake
        """
        return self.stars.count()


class Comment(models.Model):
    """
       Defines the model for comments
    """
    bake = models.ForeignKey(Bake, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Orders the comments by the order in which they were made,
        oldest first
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class BestFor(models.Model):
    """
       Defines the model for Best For bakes
    """
    # Defines the choices for Best For bakes
    BEST_FOR_CHOICES = [
        (1, 'Brunch'),
        (2, 'Kids'),
        (3, 'Parties'),
        (4, 'Sharing'),
        (5, 'Birthdays'),
        (6, 'Christmas'),
        (7, 'Weekend Baking'),
        (8, 'Simple Baking'),
    ]

    best_for = models.IntegerField(choices=BEST_FOR_CHOICES, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bake = models.ForeignKey(Bake, on_delete=models.CASCADE)

    class Meta:
        """
        Orders the Best For bakes
        """
        ordering = ['best_for']

    def __str__(self):
        return f"Bake selected as Best For {self.best_for} by {self.user}"
