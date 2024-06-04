from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from shop.models import Comment


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control'
                               }))
    password1 = forms.CharField(label='Придумайте пароль',
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control'
                                }))
    password2 = forms.CharField(label='Подтвердите пароль',
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control'
                                }))
    email = forms.CharField(label='Введите E-mail',
                            widget=forms.EmailInput(attrs={
                                'class': 'form-control'
                            }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Введите имя пользователья',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control'
                               }))
    password = forms.CharField(label='Введите пароль',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control'
                               }))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Оставьте отзыв',
                'rows': 5
            })
        }





