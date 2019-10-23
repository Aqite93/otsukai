from django import forms
from .models import Errand, Category


class ErrandIndexForm(forms.ModelForm):

    class Meta:
        model = Errand
        fields = ('image', 'description', 'category', 'deadline', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


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
        label='Price'
    )

    image = forms.FileField(
        widget=forms.FileInput(
            attrs={
                "style": "display:none",
                "id": "uploadFile"
            }
        )
    )

    description = forms.CharField(
        label='Description',
        max_length=1024,
        widget=forms.Textarea()
    )

    class Meta:
        model = Errand
        fields = ('category', 'deadline', 'price', 'image', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
