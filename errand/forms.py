from django import forms
from .models import Errand


class ErrandIndexForm(forms.ModelForm):
    description = forms.CharField(
        label='Description',
        max_length=1024,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'パスワードを半角英数字記号を組み合わせた8桁以上で入力してください．'
            }
        )
    )

    class Meta:
        model = Errand
        fields = ('description',)
