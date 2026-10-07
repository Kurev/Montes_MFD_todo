from django.test import TestCase
from django.urls import reverse

from .models import List


class TodoListViewTests(TestCase):
    def test_home_post_creates_item_and_renders_it(self):
        response = self.client.post(reverse('home'), {'item': 'Buy milk'}, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(List.objects.filter(item='Buy milk').exists())
        self.assertContains(response, 'Buy milk')
