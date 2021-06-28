from django import forms
from django.forms import ModelForm
from .models import News, Category
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.models import UserCreationForm

import re


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

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
        widget = {}
