from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class Review(models.Model):
    name = models.CharField(max_length=32)
    text = models.TextField()
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    def get_absolute_url(self):
        return reverse('list')

    def __str__(self):
        return self.text
