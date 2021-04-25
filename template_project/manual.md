# Many-to-Many

```python
class Developers(Model):
    name = CharField(max_length=50, verbose_name='Имя')

class Tasks(Model):
    developers = ManyToManyField(Developers, related_name='tasks', verbose_name='Разработчики')

```