from django import forms


class UserForm(forms.Form):
    name = forms.CharField(required=False)
    age = forms.IntegerField()