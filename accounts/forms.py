from django import forms
from .models import User


class UserForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'メールアドレスを入力してください．'
            }
        )
    )

    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'パスワードを半角英数字記号を組み合わせた8桁以上で入力してください．'
            }
        )
    )

    class Meta:
        model = User
        fields = ('email', 'password')
