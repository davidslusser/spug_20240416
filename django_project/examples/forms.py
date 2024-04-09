from django import forms
from examples.models import MyModel


class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['data']
        widgets = {
                    'data': forms.TextInput(attrs={'class': 'form-control'}),
                }
