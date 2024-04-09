from django.db import models


class Dairy_strings(models.Model):
    title = models.CharField('Тема', max_length=50)
    main_field = models.TextField('Событие')
    date = models.DateTimeField('Дата записи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

# Create your models here.
