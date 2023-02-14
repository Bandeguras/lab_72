from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
CATEGORY_CHOICES = [('new', 'Новый'), ('on moderate', 'На модерацию')]
# Create your models here.


class Quote(models.Model):
    text = models.TextField(max_length=3000, verbose_name="Текст")
    name = models.CharField(max_length=30, verbose_name="Автор")
    email = models.EmailField(max_length=254)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    status = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                                    verbose_name="Категория")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата начала")


