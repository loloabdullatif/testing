from django import forms


class Memberform(forms.Form):
    first_name = forms.CharField(label="first name", max_length=100)
    last_name = forms.CharField(label="last name", max_length=100)