from django import forms


class FormName(forms.Form):
    name = forms.CharField()
    url = forms.CharField(widget=forms.URLInput)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)


