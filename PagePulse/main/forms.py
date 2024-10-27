from django import forms

class SignUpForm(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        required=True
    )
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Date of Birth'}),
        required=True
    )
    terms = forms.BooleanField(
        required=True,
        label="I agree to the Terms & Conditions"
    )
