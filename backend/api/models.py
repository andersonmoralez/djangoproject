from django.db import models
from model_utils.models import TimeStampedModel

class EventRegister(TimeStampedModel):
    name = models.CharField(max_length=25, verbose_name='Name')
    surname = models.CharField(max_length=25, verbose_name='Surname')
    password = models.CharField(max_length=300, verbose_name='Password')
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        import hashlib
        hash = hashlib.sha256()
        hash.update(self.password.encode())
        self.password = hash.digest()
        super(EventRegister, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Event Register'
        verbose_name_plural = 'Event Register'
        ordering = ['-created']
