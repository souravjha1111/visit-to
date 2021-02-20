from django import forms

from .validators import validate_url

class SubmitForm(forms.Form):
    shortcode = forms.CharField(label='ShortCode', required =False, widget = forms.TextInput(
        attrs = {
            
            "placeholder": "Enter Your shortcode",
            "class": "form-control text_change"}))
    url = forms.CharField(label='Enter Url .',widget = forms.TextInput(
        attrs = {
            "placeholder": "Enter Your Url Here",
            "class": "form-control text_change"}))
