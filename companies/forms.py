from django import forms


class CompanySearchForm(forms.Form):
    client = forms.CharField(max_length=32)
    name = forms.CharField(max_length=32)
    code = forms.CharField(max_length=32)
    email = forms.CharField(max_length=32)
    survey = forms.CharField(max_length=32)
    contract = forms.CharField(max_length=32)
