# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class AppUsers(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True,null=True)
    last_name = models.CharField(max_length=100, blank=True,null=True)

    class Meta:
        app_label = 'app'
        db_table = 'app_users'

class Applications(models.Model):
    app_id = models.AutoField(primary_key=True)
    app_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True,null=True)
    created_by = models.ForeignKey(AppUsers, related_name='created_by')
    updated_by = models.ForeignKey(AppUsers, related_name='updated_by', blank=True, null=True)

    class Meta:
        app_label = 'app'
        db_table = 'applications'

