"""
Imports external libraries for the program
"""
from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published")


class Bake(models.Model):
     """
       Defines the main class of model for bakes
    """
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    slug = AutoSlugField(populate_from=['title', 'description'])
    difficulty = models.IntegerField(choices=[1, 2, 3, 4, 5], default=3)
    equipment = models.TextField(max_length = 200)
    ingredients = models.TextField()
    method = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    stars = models.ManyToManyField(User, related_name='bake_stars', blank=True)

    class Meta:
        """
        Orders the bakes by the order in which they were posted,
        most recent first
        """
        ordering = ['-created_on']

        def __str__(self):
            return self.title

        def number_of_stars(self):
            return self.stars.count()




     