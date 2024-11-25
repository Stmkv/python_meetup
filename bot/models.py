from django.db import models


class User(models.Model):
    tg_id = models.CharField(
        'телеграм id',
        max_length=50,
        blank=True,
    )
    name = models.CharField(
        'Имя',
        max_length=50,
        blank=True
    )
    company = models.CharField(
        'Компания',
        max_length=100,
        blank=True
    )
    position = models.CharField(
        'Должность',
        max_length=100,
        blank=True
    )
    STATUS_CHOICES = [
        ('PARTICIPANT', 'Участник'),
        ('SPEAKER', 'Спикер')
    ]
    status = models.CharField(
        'Статус',
        max_length=50,
        choices=STATUS_CHOICES,
        default='PARTICIPANT'
    )

    def __str__(self) -> str:
        return f'{self.firstname} - {self.tg_id}'
  
    class Meta:
        verbose_name = 'Участник',
        verbose_name_plural = 'Участники'
