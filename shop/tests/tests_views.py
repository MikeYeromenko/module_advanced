from django.test import TestCase
from django.urls import reverse, reverse_lazy

from shop.models import AdvUser


def create_user(username='test_user', password='testpass1234', email='test_email@somesite.com'):
    return AdvUser.objects.create(username=username, password=password, email=email)


class UserRegistrationTests(TestCase):

    def test_login(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        user = create_user()
        response = self.client.post(reverse('shop:login'), {'username': user.username, 'password': user.password})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertTrue(response.context['user'].is_authenticated)
        # self.assertRedirects(response, reverse_lazy('shop:profile'))
        user2 = create_user(username='test_user2')

        # check, the redirect page after login is 'next'
        response1 = self.client.get(reverse('shop:profile_change'))
        self.assertEqual(response.status_code, 300)
        self.assertRedirects(response1, reverse_lazy('shop:login'))
        print(f'Fuck you')
