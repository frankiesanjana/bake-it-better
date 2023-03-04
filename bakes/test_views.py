from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Bake


class TestViews(TestCase):

    def setUp(self):
        """
        Creates test objects to perform view testing
        """
        self.user = User.objects.create_user(username='test_user', password='test')
        self.bake = Bake.objects.create(title='title', author=self.user, description='description', difficulty=1, equipment='equipment', ingredients='ingredients', method='method', featured_image='placeholder', status=1)

    def tearDown(self):
        """
        Deletes test objects used to perform view testing
        """
        User.objects.all().delete()
        Bake.objects.all().delete()

    def test_can_get_bake_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_can_get_bake_detail_page(self):
        response = self.client.get(f'/bake-detail/{self.bake.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bake-detail.html')

    def test_can_get_signup_page(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_can_get_login_page(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_can_get_add_bake_page(self):
        self.client.login(username='test_user', password='test')
        response = self.client.get('/add-bake/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add-bake.html')

    def test_can_get_edit_bake_page(self):
        self.client.login(username='test_user', password='test')
        response = self.client.get(f'/edit-bake/{self.bake.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit-bake.html')

    def test_can_get_delete_bake_page(self):
        self.client.login(username='test_user', password='test')
        response = self.client.get(f'/delete-bake/{self.bake.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete-bake.html')

    def test_can_get_best_for_bakes_page(self):
        self.client.login(username='test_user', password='test')
        response = self.client.get('/bestforbakes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'best-for-bakes.html')
    
    def test_can_get_my_starred_bakes_page(self):
        self.client.login(username='test_user', password='test')
        response = self.client.get('/mystarredbakes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my-starred-bakes.html')

    def test_can_get_logout_page(self):
        self.client.login(username='test_user', password='test')
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/logout.html')

    def test_can_add_bake(self):
        self.client.login(username='test_user', password='test')
        self.client.post(f'/add-bake/', {
                        'title': 'test title',
                        'author': self.user,
                        'description': 'test description',
                        'difficulty': 1,
                        'equipment': 'test equipment',
                        'ingredients': 'test ingredients',
                        'method': 'test method',
                        'featured_image': 'placeholder',
                        'status': 0
                         })
        new_bake = Bake.objects.filter(title='test title')
        self.assertTrue(new_bake)
        

    def test_can_edit_bake(self):
        self.client.login(username='test_user', password='test')
        self.client.get(f'/edit-bake/{self.bake.slug}/', {
                        'title': 'new title',
                        'author': self.user,
                        'description': 'new description',
                        'difficulty': 2,
                        'equipment': 'new equipment',
                        'ingredients': 'new ingredients',
                        'method': 'new method',
                        'featured_image': 'placeholder',
                        'status': 1
                         })
        edited_bake = Bake.objects.first()
        self.assertTrue(edited_bake)

    def test_can_delete_bake(self):
        self.client.login(username='test_user', password='test')
        self.client.post(f'/add-bake/', {
                        'title': 'another title',
                        'author': self.user,
                        'description': 'another description',
                        'difficulty': 1,
                        'equipment': 'another equipment',
                        'ingredients': 'another ingredients',
                        'method': 'another method',
                        'featured_image': 'placeholder',
                        'status': 0
                         })
        response = self.client.post(f'/delete-bake/another-title/')
        deleted_bake = Bake.objects.filter(title='another title')
        self.assertFalse(deleted_bake)
    
        def test_can_star_bake(self):
            self.client.login(username='test_user', password='test')
            self.client.post(f'/add-bake/', {
                            'title': 'star title',
                            'description': 'star description',
                            'difficulty': 1,
                            'equipment': 'star equipment',
                            'ingredients': 'star ingredients',
                            'method': 'star method',
                            'featured_image': 'placeholder',
                            'status': 1,
                            'starred': True
                            })
            star_bake = Bake.objects.filter(title='star title')
            response = self.client.post(f'/star/star-title/')
            self.assertRedirects(response, f'/bake-detail/star-title/')
            starred_bake = get_object_or_404(star_bake, slug="star-title")
            num_stars = len(starred_bake.stars.all())
            self.assertEqual(num_stars, 1)