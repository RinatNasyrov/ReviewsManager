from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    name = models.CharField(max_length=32)
    text = models.TextField()
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.text
