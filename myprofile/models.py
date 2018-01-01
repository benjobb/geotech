from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.db import models
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)


class Profile(models.Model):
    project = models.ForeignKey(Project, related_name = 'projectprofile_set')
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    water_table_depth = models.DecimalField(decimal_places=2,max_digits=4, default=0)


    def get_absolute_url(self):
        return reverse('profile-update', kwargs={'profile_pk': self.pk})

    def __unicode__(self):
        return "%s" % (self.name)


class Layers(models.Model):
    profile = models.ForeignKey(Profile, related_name = 'profilelayer_set')
    name = models.CharField(max_length=100)
    depth = models.DecimalField(decimal_places = 2, max_digits = 5, default =0)
    SPT_N_Value = models.IntegerField(default=0)
