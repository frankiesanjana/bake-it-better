from django.test import TestCase
from .forms import BakeForm, CommentForm, BestForForm


class TestBakeForm(TestCase):
    """
    Provides automated tests for the form BakeForm
    """
    def test_title_is_required(self):
        form = BakeForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_equipment_is_required(self):
        form = BakeForm({'equipment': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('equipment', form.errors.keys())
        self.assertEqual(form.errors['equipment'][0],
                         'This field is required.')

    def test_ingredients_is_required(self):
        form = BakeForm({'ingredients': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('ingredients', form.errors.keys())
        self.assertEqual(form.errors['ingredients'][0],
                         'This field is required.')

    def test_method_is_required(self):
        form = BakeForm({'method': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('method', form.errors.keys())
        self.assertEqual(form.errors['method'][0], 'This field is required.')

    def test_description_is_not_required(self):
        form = BakeForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertNotIn('description', form.errors.keys())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = BakeForm()
        self.assertEqual(
            form.Meta.fields, ['title', 'description', 'difficulty',
                               'equipment', 'ingredients', 'method',
                               'featured_image', 'status'])


class TestCommentForm(TestCase):
    """
    Provides automated tests for the form CommentForm
    """
    def test_body_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))


class TestBestForForm(TestCase):
    """
    Provides automated tests for the form BestForForm
    """
    def test_best_for_is_required(self):
        form = BestForForm({'best_for': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('best_for', form.errors.keys())
        self.assertEqual(form.errors['best_for'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = BestForForm()
        self.assertEqual(form.Meta.fields, ('best_for',))
