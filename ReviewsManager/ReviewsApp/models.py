from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class Review(models.Model):
    name = models.CharField(max_length=32,verbose_name='Имя')
    text = models.TextField(verbose_name='Текст')
    rate = models.IntegerField(verbose_name='Оценка', validators=[MinValueValidator(1), MaxValueValidator(5)])
    def get_absolute_url(self):
        return reverse('list')

    def __str__(self):
        return self.text
