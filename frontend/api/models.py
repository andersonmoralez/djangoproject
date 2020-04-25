from django.db import models
from model_utils.models import TimeStampedModel

class EventRegister(TimeStampedModel):
    name = models.CharField(max_length=25, verbose_name='Name')
    sobrenome = models.CharField(max_length=25, verbose_name='Sobrenome')
    senha = models.CharField(max_length=8, verbose_name='Senha')
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Event Register'
        verbose_name_plural = 'Event Register'
        ordering = ['-created']
