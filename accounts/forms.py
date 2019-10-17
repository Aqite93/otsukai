from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'メールアドレスを入力してください．'
            }
        )
    )

    password1 = forms.CharField(
        label='Password1',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'パスワードを半角英数字記号を組み合わせた8桁以上で入力してください．'
            }
        )
    )

    password2 = forms.CharField(
        label='Password2',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'パスワードを半角英数字記号を組み合わせた8桁以上で入力してください．'
            }
        )
    )

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
