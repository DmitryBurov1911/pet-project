from django import forms
from men.models import Category
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"

    class Meta:
        model = Men
        fields = ["title", "slug", "content", "photo", "is_published", 'category']

        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'form-input'
            }), 
            "content": forms.Textarea(attrs={
                'cols': 60, 
                'rows': 10
            })
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise forms.ValidationError('Длина превышает 200 символов')

        return title

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='LOGIN',  widget = forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Ваш EMAIL', widget = forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Ваш пароль', widget = forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля',  widget = forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

