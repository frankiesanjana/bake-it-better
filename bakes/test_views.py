from django.test import TestCase
from django.contrib.auth.models import User
from .models import Bake


class TestViews(TestCase):

    def setUp(self):
        """
        Creates test objects to perform view testing
        """
        self.user = User.objects.create_user(username='test_user', password='test')
        self.bake = Bake.objects.create(title='title', author=self.user, description='description', difficulty=1, equipment='equipment', ingredients='ingredients', method='method', featured_image='placeholder', status=0)

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

    # this one doesn't work
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

