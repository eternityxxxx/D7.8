from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    age = models.PositiveSmallIntegerField(null=True, blank= True, verbose_name='Возраст')
    photo = models.ImageField(upload_to='user_photo', null=True, blank=True, verbose_name='Фото')
    user = models.OneToOneField(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='profile_user',
        verbose_name='Аккаунт'
    )

    def __str__(self):
        return str(self.user)
