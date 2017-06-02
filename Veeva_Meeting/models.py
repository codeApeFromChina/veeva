# coding:utf-8
import uuid

import datetime
from django.db import models


def now() :
	n = datetime.now()
	return int(datetime.time.mktime(n.timetuple()))


class Person(models.Model) :
	'''
	人员model
	'''
	person_id = models.UUIDField(default = uuid.uuid4, null = False, help_text = "person_id",
	                             verbose_name = u'Person uuid', )
	person_name = models.CharField(max_length = 50)


class Speaker(models.Model) :
	'''
	主讲人model
	'''
	speaker_id = models.UUIDField(default = uuid.uuid4, null = False, help_text = "speaker_id",
	                              verbose_name = u'Speaker uuid', )
	speaker_name = models.CharField(max_length = 50)


class Meeting(models.Model) :
	'''
	会议model
	'''
	meeting_id = models.UUIDField(default = uuid.uuid4, null = False, verbose_name = u'meeting uuid',
	                              help_text = u"meeting_id", )
	meeting_name = models.CharField(max_length = 100)
	meeting_date = models.BigIntegerField(default = now)
	meal_fee = models.FloatField(default = 0)
	gift_fee = models.FloatField(default = 0)
	site_cost = models.FloatField(default = 0)
	approval_flag = models.CharField(max_length = 1)
	speaker = models.OneToOneField(Speaker)
	member = models.ManyToManyField(Person, through = "MeetingPersonRealtion")


class MeetingPersonRealtion(models.Model) :
	'''
	会议-人员关系model
	'''
	meeting_person_id = models.UUIDField(default = uuid.uuid4, null = False, help_text = "meeting_person_realtion_id",
	                                     verbose_name = u'meeting_person_realtion uuid', )
	person = models.ForeignKey(Person)
	meeting = models.ForeignKey(Meeting)