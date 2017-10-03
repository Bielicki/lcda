from django import forms


class ContactSearchForm(forms.Form):
    company = forms.CharField(max_length=64)
    name = forms.CharField(max_length=32)
    surname = forms.CharField(max_length=32)
    email = forms.EmailField()