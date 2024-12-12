

from django import forms

class EmailForm(forms.Form):
    recipients = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter email addresses separated by commas'}),
        label='Recipients',
        required=True
    )
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


