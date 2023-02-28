from django.test import TestCase
from .forms import BakeForm, CommentForm, BestForForm


class TestBakeForm(TestCase):

    def test_title_is_required(self):
        form = BakeForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_equipment_is_required(self):
        form = BakeForm({'equipment': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('equipment', form.errors.keys())
        self.assertEqual(form.errors['equipment'][0], 'This field is required.')
    
    def test_ingredients_is_required(self):
        form = BakeForm({'ingredients': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('ingredients', form.errors.keys())
        self.assertEqual(form.errors['ingredients'][0], 'This field is required.')
    
    def test_method_is_required(self):
        form = BakeForm({'method': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('method', form.errors.keys())
        self.assertEqual(form.errors['method'][0], 'This field is required.')
    
    def test_description_is_not_required(self):
        form = BakeForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertNotIn('description', form.errors.keys())