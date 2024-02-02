from django import forms
from .models import Review

class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name','text','rate']
        labels = {
            'name' : 'Имя',
            'text': 'Текст',
            'rate': 'Оценка'
        }