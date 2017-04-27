import logging
from datetime import date

from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404

logger = logging.getLogger("MangaTime.administration.models")

class User(AbstractUser):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=90, null=True, blank=True)
    language = models.CharField(max_length=10, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE, null=True)

    class Meta:
        db_table = 'users'
        verbose_name = _('User')
        verbose_name_plural = _('Users')
