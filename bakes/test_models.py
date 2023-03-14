from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Bake


class TestModels(TestCase):
    """
    Class created to test the models in bakes/models.py
    """

    def setUp(self):
        """
        Creates test objects to perform model testing
        """
        self.user = User.objects.create_user(
            username='test_user', password='test')
        self.bake = Bake.objects.create(
            title='title', author=self.user, description='description',
            difficulty=1, equipment='equipment', ingredients='ingredients',
            method='method', featured_image='placeholder', status=0)

    def tearDown(self):
        """
        Deletes test objects used to perform model testing
        """
        User.objects.all().delete()
        Bake.objects.all().delete()

    def test_bake_slug_created_from_title(self):
        """
        Tests that slug is created from title
        """
        self.assertEqual(self.bake.slug, 'title')

    def test_bake_string_created(self):
        """
        Tests that string is created in bake model
        """
        self.assertEqual(str(self.bake.title), 'title')

    def test_bake_stars_defaults_to_false(self):
        """
        Tests that a newly created bake defaults to unstarred
        """
        star_bake = Bake.objects.filter(title='title')
        star_bake_test = get_object_or_404(star_bake, slug="title")
        num_stars = len(star_bake_test.stars.all())
        self.assertNotEqual(num_stars, 1)
