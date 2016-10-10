# -*- coding: utf-8 -*-#
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext as _
from registration.forms import RegistrationFormUniqueEmail
from crm.widgets import userWidget, usersWidget, phoneWidget, mobilePhoneWidget, passwordWidget, emailWidget

__author__ = 'AMA'


class MyRegistrationFormUniqueEmail(RegistrationFormUniqueEmail):

    username = forms.RegexField( label=_("Логин"), max_length=30, regex=r"^[\w.@+-]+$",
        error_messages={ 'invalid': _("< 30 симоволов.сДопустимо только - A-z,1-9,@/./+/-/")},
        widget=userWidget(attrs={'class': 'form-control','required': 'true', 'placeholder': _('Логин ( только A-z,1-9,@/./+/-/_ )')}))

    email = forms.CharField(label=_("Электронная почта"),
                            widget=emailWidget(
                            attrs={'class': 'form-control', 'type': 'email', 'placeholder': _('Электронная почта'), 'required': 'true'}))

    password1 = forms.CharField( label=_("Пароль"),
                                 widget=passwordWidget(
                                 attrs={'class': 'form-control',
                                        'required': 'true',
                                        'type': 'password',
                                        'placeholder': _('Пароль. Не менее 8 знаков, буквы и цифры')}) )

    password2 = forms.CharField( label=_("Подтверждение пароля"), widget=passwordWidget(
                                                                  attrs={'class': 'form-control',
                                                                        'required': 'true',
                                                                        'type': 'password',
                                                                        'placeholder': _('Подтверждение пароля. Оба пароля должны совпадать.'),}))

class MyAuthenticationForm( AuthenticationForm ):

    username = forms.RegexField(label=_("Логин"), max_length=30, regex=r"^[\w.@+-]+$",
                                error_messages={'invalid': _("< 30 симоволов. Допустимо только - A-z,1-9,@/./+/-/")},
                                widget=userWidget(attrs={'class': 'form-control', 'required': 'true', 'placeholder': _('Логин')}))

    password = forms.CharField(label=_("Пароль"),
                                widget=passwordWidget(
                                    attrs={'class': 'form-control', 'required': 'true', 'placeholder': _('Пароль')}))