from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def index(request):
    context = {'hello': _('Hello')}

    return render(request, 'shop/index.html', context)
