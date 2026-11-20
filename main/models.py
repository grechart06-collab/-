from django.db import models

# Create your models here.
class Мероприятие(models.Model):
    event_name = models.CharField('Название')
    event_text = models.TextField('Описание мероприятия')
    date = models.DateTimeField('Дата публикации')
