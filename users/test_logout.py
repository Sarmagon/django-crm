from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class LogoutTests(TestCase):
    def test_sidebar_logout_requires_csrf_and_ends_session(self):
        user = get_user_model().objects.create_user(username="logout-test")
        client = Client(enforce_csrf_checks=True)
        client.force_login(user)
        response = client.get("/")
        self.assertContains(response, 'action="' + reverse("logout") + '"')
        self.assertEqual(client.get(reverse("logout")).status_code, 405)
        self.assertEqual(client.post(reverse("logout")).status_code, 403)
        token = client.cookies["csrftoken"].value
        response = client.post(reverse("logout"), {"csrfmiddlewaretoken": token})
        self.assertRedirects(response, reverse("login"), fetch_redirect_response=False)
        self.assertNotIn("_auth_user_id", client.session)
