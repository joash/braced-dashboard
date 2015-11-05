from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.conf import settings
from datetime import datetime

# Documentation
class DocumentationApp(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    documentation = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('create_date',)

    def save(self):
        if self.create_date is None:
            self.create_date = datetime.now()
        super(DocumentationApp, self).save()

    def __unicode__(self):
        return unicode(self.name)


class DocumentationAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'documentation', 'create_date',)
    display = 'DocumentationApp'


# collect feedback from users
class Feedback(models.Model):
    submitter = models.ForeignKey(settings.AUTH_USER_MODEL)
    note = models.TextField()
    page = models.CharField(max_length=135)
    severity = models.CharField(max_length=135)
    create_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('create_date',)

    def save(self):
        if self.create_date is None:
            self.create_date = datetime.now()
        super(Feedback, self).save()

    def __unicode__(self):
        return unicode(self.submitter)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('submitter', 'note', 'page', 'severity', 'create_date',)
    display = 'Feedback'


# FAQ
class FAQ(models.Model):
    question = models.TextField(null=True, blank=True)
    answer =  models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('create_date',)

    def save(self):
        if self.create_date is None:
            self.create_date = datetime.now()
        super(FAQ, self).save()

    def __unicode__(self):
        return unicode(self.question)


class FAQAdmin(admin.ModelAdmin):
    list_display = ( 'question', 'answer', 'create_date',)
    display = 'FAQ'