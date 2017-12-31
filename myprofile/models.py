from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.db import models
from django.utils import timezone


class Profile(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('profile-update', kwargs={'pk': self.pk})

    def __unicode__(self):
        return "%s %s" % (self.name)


class Layers(models.Model):
    profile = models.ForeignKey(Profile, related_name = 'profilelayer_set')
    name = models.CharField(max_length=100)
    depth = models.DecimalField(decimal_places = 2, max_digits = 5, default =0)
    SPT_N_Value = models.IntegerField(default=0)
