from .models import Dairy_strings
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea



class Dairy_stringsForm(ModelForm):
    class Meta:
        model = Dairy_strings
        fields = ['title', 'main_field', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема события'
            }),
            'main_field': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Событие'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            })
        }