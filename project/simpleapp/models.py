from django.db import models
from django.core.validators import MinValueValidator


# Создаём модель новости
class New(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,  # названия новостей не должны повторяться
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news',  # все новости в категории будут доступны через поле news
    )
    price = models.FloatField(
        validators=[MinValueValidator(0.0)],
    )
    auto_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):  # добавим абсолютный путь чтобы после создания нас перебрасывало на страницу с new
        return f'/news/{self.id}'


#  создаём категорию, к которой будет привязываться новость
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # названия категорий тоже не должны повторяться

    def __str__(self):
        return f'{self.name.title()}'