from django import forms
from .models import Errand, Category


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


class ErrandRegisterForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        label='Category',
        queryset=Category.objects.all()
    )

    deadline = forms.DateTimeField(
        label='Deadline',
        required=True,
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=['%Y-%m-%d']
    )

    price = forms.IntegerField(
        label='Price',
        widget=forms.Textarea()
    )

    image = forms.FileField()

    comments = forms.CharField(
        label='Description',
        max_length=1024,
        widget=forms.Textarea()
    )

    class Meta:
        model = Errand
        fields = ('category', 'deadline', 'price', 'image', 'comments')
