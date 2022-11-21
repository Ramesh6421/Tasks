from django import forms 
from .models import Todo,User
from django.contrib.auth.forms import UserCreationForm

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo 
        fields = ['title','is_finished']    

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','password1','password2']