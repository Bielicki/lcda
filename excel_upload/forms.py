from django.forms import forms


class ExcelForm(forms.Form):
    excel = forms.FileField()
