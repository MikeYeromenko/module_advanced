from django.contrib.auth import forms as auth_f
from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _

from module import settings
from shop.models import AdvUser, user_registrated


class UserAuthenticationForm(auth_f.AuthenticationForm):

    def __init__(self, request=None, *args, **kwargs):
        auth_f.AuthenticationForm.__init__(self, request, *args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Username'),
                                                    'type': 'text'})
        self.fields['username'].label = ''

        self.fields['password'].widget.attrs.update({'autocomplete': 'current-password', 'class': 'form-control',
                                                     'placeholder': _('Password'), 'type': 'text'})
        self.fields['password'].label = ''


class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control',
                                                              'placeholder': _('Password')}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control',
                                                              'placeholder': _('Repeat password')}))

    class Meta:
        model = AdvUser
        fields = ['username', 'password1', 'password2', 'email', 'send_messages']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Username'),
                                                      'type': 'text'}),
                   'wallet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Last name'),
                                                    'type': 'text', 'readonly': 'readonly'}),
                   'send_messages': forms.CheckboxInput(attrs={'style': 'width: 1.5em; height: 1.5em;'}),
                   'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Email'),
                                                   'type': 'text'})
                   }

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1, password2 = self.cleaned_data.get('password1'), self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(_('Passwords mismatch'), code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        user.is_activated = False
        user.wallet = settings.DEFAULT_SUM_FOR_USER
        if commit:
            user.save()
        user_registrated.send(UserCreateForm, instance=user)
        return user


class UserUpdateForm(forms.ModelForm):
    wallet = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'disabled': 'True'
                                                           }),
                             required=False)

    class Meta:
        model = AdvUser
        fields = ['username', 'first_name', 'last_name', 'wallet', 'email', 'send_messages']

        widgets = UserCreateForm.Meta.widgets.copy()
        widgets.update({'first_name': forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': _('First name'), 'type': 'text'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Last name'),
                                                'type': 'text'})
        })


