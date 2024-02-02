from django import forms
from .models import Review

class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name','text','rate']
        #Здесь можно так, но в фильтрах так переименовать не получается, только verbose_name='...'
        # labels = {
        #     'name': 'Имя',
        #     'text': 'Текст',
        #     'rate': 'Оценка'
        # }