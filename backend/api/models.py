from django.db import models
from model_utils.models import TimeStampedModel
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save

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

def token_request(request):
    try:
        new_token = Token.objects.get_or_create(user=request.user)
        return JsonResponse({'token': new_token[0].key}, status=status.HTTP_200_OK)
    except Exception as message:
        return JsonResponse({'messagem': 'você não tem permissão.'}, status=status.HTTP_401_UNAUTHORIZED)