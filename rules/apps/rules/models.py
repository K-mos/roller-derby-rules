# -*- coding:utf-8 -*-
from django.db import models


class Rule(models.Model):
    """
    Rule model
    """
    section = models.ForeignKey('Section', null=True, blank=True)
    number = models.CharField(max_length=10, unique=True)
    content = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)
    last_edition = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["number"]

    def __unicode__(self):
        return u'%s' % self.number


class Section(models.Model):
    """
    Section model
    """
    number = models.CharField(max_length=10, unique=True)
    label = models.CharField(max_length=255)
    creation = models.DateTimeField(auto_now_add=True)
    last_edition = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["number"]

    def __unicode__(self):
        return u'%s' % self.label