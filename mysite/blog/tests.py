
from django.test import TestCase
from django.urls import reverse


class PostViewTests(TestCase):

    def test_post_list_status_code(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)

    def test_post_list_template(self):
        response = self.client.get(reverse("post_list"))
        self.assertTemplateUsed(response, "blog/post_list.html")

    def test_post_detail_not_found(self):
        response = self.client.get(
            reverse("post_detail", kwargs={"pk": 999999})
        )
        self.assertEqual(response.status_code, 404)

    def test_hello_world(self):
        response = self.client.get(reverse("hello_world"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello World")