from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.charField(max_length=31)
    slug = models.SlugField()

class Person(models.Model):
    f_name = models.CharField(max_length=31)
    m_name = models.CharField(max_length=31)
    s_name = models.CharField(max_length=31)
    slug = models.SlugField()
    desc = models.TextField()
    joined_date = models.DateField()
    e_mail = models.EmailField()
    



class DateEvent(models.Model):
    pass


class DateCalendar(models.Model):
    pass


class DateEventMedia(models.Model):
    pass
