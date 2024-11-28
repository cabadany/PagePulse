from django import forms

class PasswordResetForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address', 'class': 'input-field'}))
