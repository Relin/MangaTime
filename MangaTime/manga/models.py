import logging
from datetime import date

from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404

from MangaTime.administration.models import User
from MangaTime.people.models import People

logger = logging.getLogger("MangaTime.manga.models")

class countryEnum(object):
    JAPAN = 1
    KOREA = 2
    CHINA = 3
    FRANCE = 4

    CHOICES = (
        (JAPAN, _('Japan')),
        (KOREA, _('Korea')),
        (CHINA, _('China')),
        (FRANCE, _('France')),
    )

class Mangaz (models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90)
    start_date = models.DateField(null=True, blank=True, default=None)
    end_date = models.DateField(null=True, blank=True, default=None)
    nb_vol = models.IntegerField(null=True, blank=True, default=None)
    country = models.CharField(max_length=90, choices=countryEnum.CHOICES, default=countryEnum.JAPAN)
    picture = models.ImageField(upload_to='documents/manga/', null=True, blank=True, default=None)
    writer = models.ForeignKey(People, related_name='writer', null=True, blank=True, default=None)
    drawer = models.ForeignKey(People, related_name='drawer', null=True, blank=True, default=None)

    def __str__(self):
        return self.term_name

    class Meta:
        db_table = 'mangazs'
        verbose_name = _('Mangaz')
        verbose_name_plural = _('Mangazs')

class MangaProgress (models.Model):

    id = models.AutoField(primary_key=True)
    manga = models.ForeignKey(Mangaz)
    user = models.ForeignKey(User)
    nb_vol_buy = models.IntegerField(null=True, blank=True, default=None)
    nb_vol_read = models.IntegerField(null=True, blank=True, default=None)
    done = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'mangaprogress'
        verbose_name = _('MangaProgress')
        verbose_name_plural = _('MangasProgress')
