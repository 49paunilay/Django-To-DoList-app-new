from django import forms
from .models import Todoclass

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todoclass
        fields=('header','main_text')