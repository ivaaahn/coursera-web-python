from typing import DefaultDict
from django.utils.translation import gettext_lazy as _
from django.db.models import *

# Create your models here.

class Developers(Model):
    class Level(TextChoices):
        FRESHMAN = 'FR', 'Freshman'
        JUNIOR = 'JR', 'Junior'
        MIDDLE = 'ML', 'Middle'
        SENIOR = 'SR', 'Senior' 

    class Sex(IntegerChoices):
        MALE = 0, 'Male'
        FEMALE = 1, 'Female'


    name = CharField(max_length=50, verbose_name='Имя')
    age = IntegerField(null=False, verbose_name='Возраст')
    sex = IntegerField(choices=Sex.choices, default=Sex.MALE)
    level = CharField(max_length=2, choices=Level.choices, default=Level.JUNIOR, verbose_name='Уровень')
    rating = FloatField()
    email = EmailField(max_length=100, verbose_name='Эл. почта')
    registrDate = DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')


    def __str__(self) -> str:
        return f'{self.id}. {self.name} ({self.level}); rating: {self.rating}'


    class Meta:
        verbose_name = 'разработчик'
        verbose_name_plural = 'разработчики'



class Tasks(Model):
    class Complexity(IntegerChoices):
        EASY = 0, 'Easy'
        AVERAGE = 1, 'Average'
        HARD = 2, 'Hard'

    title = CharField(max_length=50, verbose_name='Название')
    startDate = DateTimeField(auto_now_add=True, verbose_name='Время получения задания')
    complexity = IntegerField(choices=Complexity.choices, default=Complexity.AVERAGE, verbose_name='Сложность')
    developers = ManyToManyField(Developers, related_name='tasks', verbose_name='Разработчики')


    def __str__(self) -> str:
        return f'{self.id}. {self.title}. Сложность: {self.complexity}. ({self.startDate})'

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        

