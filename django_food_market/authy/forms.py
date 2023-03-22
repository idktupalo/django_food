from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 
            'password1', 'password2', 
            'email'
            ]