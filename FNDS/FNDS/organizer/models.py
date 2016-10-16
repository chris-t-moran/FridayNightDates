from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField(unique = True)

    def __unicode__(self):
        return self.name

class Person(models.Model):
    f_name = models.CharField(max_length=31)
    m_name = models.CharField(max_length=31)
    s_name = models.CharField(max_length=31)
    slug = models.SlugField(unique = True)
    desc = models.TextField()
    joined_date = models.DateField()
    e_mail = models.EmailField()
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.slug



class DateEventMedia(models.Model):
    link = models.URLField()


class DateEvent(models.Model):
    desc = models.TextField()
    calendardate = models.DateField()
    dateMedia = models.ForeignKey(DateEventMedia)
    slug = models.SlugField(unique  = True)
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.slug


class DateCalendar(models.Model):
    dateEvent = models.ForeignKey(DateEvent)
    romeo = models.ForeignKey(Person, related_name='Romeo')
    juliet = models.ForeignKey(Person, related_name='Juliet')

    def __unicode__(self):
        return "{}:{}:{}".format(self.romeo, self.juliet, self.dateEvent)
