import logging
from datetime import date

from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404

logger = logging.getLogger("MangaTime.people.models")


class People (models.Model):

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, null=True, blank=True)
    bday = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.last_name + ' ' + first_name + (' (' + surname + ')' if surname else '')

    class Meta:
        db_table = 'mangas'
        verbose_name = _('Manga')
        verbose_name_plural = _('Mangas')
