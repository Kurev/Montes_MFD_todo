from django import forms

from .models import List


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['item']
        widgets = {
            'item': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add a task'}),
        }