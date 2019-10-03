from django import forms
from .models import Errand


class ErrandIndexForm(forms.ModelForm):
    description = forms.CharField(
        label='Description',
        max_length=1024,
        widget=forms.Textarea()
    )

    class Meta:
        model = Errand
        fields = ('description',)


ErrandIndexFormSet = forms.modelformset_factory(
    Errand, form=ErrandIndexForm, extra=0
)
