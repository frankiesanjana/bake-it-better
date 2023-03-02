from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Bake


class TestModels(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test')
        self.bake = Bake.objects.create(title='title', author=self.user, description='description', difficulty=1, equipment='equipment', ingredients='ingredients', method='method', featured_image='placeholder', status=0)

    def tearDown(self):
        """
        Deletes test objects used to perform view testing
        """
        User.objects.all().delete()
        Bake.objects.all().delete()
    
    # test slug is created from title
    def test_bake_slug_created_from_title(self):
        self.assertEqual(self.bake.slug, 'title')

    # test string is created in bake model
    def test_bake_string_created(self):
        self.assertEqual(str(self.bake.title), 'title')

    # test new bake defaults to unstarred by the user
    def test_bake_stars_defaults_to_false(self):
        star_bake = Bake.objects.filter(title='title')
        star_bake_test = get_object_or_404(star_bake, slug="title")
        num_stars = len(star_bake_test.stars.all())
        self.assertNotEqual(num_stars, 1)