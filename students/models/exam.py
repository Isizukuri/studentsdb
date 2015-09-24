# -*- coding: utf-8 -*-

from django.db import models
from group import Group

class Exam(models.Model):
    """Exam Model"""

    class Meta(object):
        verbose_name = u"Іспит"
        verbose_name_plural = u"Іспити"

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва")

    date_time = models.DateTimeField(
        verbose_name=u"Дата і час проведення")

    teacher_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Викладач",
        default='')

    exam_group = models.ForeignKey('Group',
        verbose_name=u"Група",
        blank=False,
        null=True)
    
    def __unicode__(self):
        if self.teacher_name:
            return u"%s (%s %s)" % (self.title, self.teacher_name,)
        else:
            return u"%s" % (self.title,)
