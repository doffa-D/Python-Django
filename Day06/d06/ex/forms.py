from django import forms
from .models import User

class SingUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        help_texts = {
            'username': "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
            'password': "Your password can’t be too similar to your other personal information. "
                        "Your password must contain at least 8 characters. "
                        "Your password can’t be a commonly used password. "
                        "Your password can’t be entirely numeric.",
        }
        error_messages = {
            'username': {
                'required': "Please enter your username",
            },
            'password': {
                'required': "Please enter your password",
            },
        }

    retry_password = forms.CharField(
        max_length=50, 
        widget=forms.PasswordInput(),
        help_text="Enter the same password as before, for verification.",
        error_messages={
            'required': "Please re-enter your password",
        }
    )
    

class SingInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
