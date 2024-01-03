from django import forms

class my_Form(forms.Form):
    history = forms.CharField(max_length=1000)