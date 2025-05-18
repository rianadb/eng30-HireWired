from django import forms

class JobSearchForm(forms.Form):
    job = forms.CharField(
        label='Search for a job',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter job title or keyword',
            'class': 'form-control'
        })
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs,pop("request", None)

        