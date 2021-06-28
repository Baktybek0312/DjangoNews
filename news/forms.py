from django import forms
from django.forms import ModelForm
from .models import News, Category
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

import re

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widget = {
           'title': forms.TextInput(attrs={'class': 'form-control'}),
           'content': forms.Textarea(attrs={'class': 'form-control', 'row': 5}),
           'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Давай без цифр')
        return title

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               help_text='Максимум до 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль',
                                help_text='Введите пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(label='Потверждение',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    email = forms.CharField(label='Электронная Почта',
                                widget=forms.EmailInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

