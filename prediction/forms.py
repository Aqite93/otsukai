from django import forms


class PredictionForm(forms.Form):
    rank = forms.CharField(
        label='insert your rank',
    )

    capacity = forms.CharField(
        label='insert your length of years',
    )

    def __init__(self, *args, **kwargs):
        super(PredictionForm, self).__init__(*args, **kwargs)
        # Set field Label as Placeholder for every field
        for field in self.fields.values():
            print(field.label)
            field.widget.attrs['placeholder'] = field.label
