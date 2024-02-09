from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class Review(models.Model):
    class Rate(models.IntegerChoices):
        #OPTIONS = [(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')]
        OPTION_1 = 1, '1'
        OPTION_2 = 2, '2'
        OPTION_3 = 3, '3'
        OPTION_4 = 4, '4'
        OPTION_5 = 5, '5'

    name = models.CharField(max_length=32,verbose_name='Имя')
    text = models.TextField(verbose_name='Текст')
    rate = models.IntegerField(max_length=2, verbose_name='Оценка', choices=Rate.choices)
    def get_absolute_url(self):
        return reverse('list')

    def __str__(self):
        return self.text
