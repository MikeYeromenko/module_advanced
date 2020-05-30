from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView, CreateView

from shop import forms
from shop.models import AdvUser


def index(request):
    context = {'hello': _('Hello')}

    return render(request, 'shop/index.html', context)


def other_page(request, page):
    try:
        template = get_template(f'shop/{page}.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


class UserLoginView(LoginView):
    authentication_form = forms.UserAuthenticationForm


class UserLogoutView(LoginRequiredMixin, LogoutView):
    pass


@login_required
def profile(request):
    return render(request, 'shop/profile.html')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = AdvUser
    form_class = forms.UserUpdateForm
    template_name = 'registration/user_update.html'

    def get_success_url(self):
        return reverse_lazy('shop:profile_change', kwargs={'pk': self.request.user.pk})


class UserCreateView(CreateView):
    model = AdvUser
    template_name = 'registration/user_register.html'
    success_url = reverse_lazy('shop:profile')
    form_class = forms.UserCreateForm

    def form_valid(self, form):
        response = super().form_valid(form)
        # login user after creation for him not to input his authentication data once again after he registered
        login(self.request, form.instance)
        return response



