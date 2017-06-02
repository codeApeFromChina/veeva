# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Veeva_Meeting.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('meeting_id', models.UUIDField(help_text='meeting_id', default=uuid.uuid4, verbose_name='meeting uuid')),
                ('meeting_name', models.CharField(max_length=100)),
                ('meeting_date', models.BigIntegerField(default=Veeva_Meeting.models.now)),
                ('meal_fee', models.FloatField(default=0)),
                ('gift_fee', models.FloatField(default=0)),
                ('site_cost', models.FloatField(default=0)),
                ('approval_flag', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='MeetingPersonRealtion',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('meeting_person_id', models.UUIDField(help_text='meeting_person_realtion_id', default=uuid.uuid4, verbose_name='meeting_person_realtion uuid')),
                ('meeting', models.ForeignKey(to='Veeva_Meeting.Meeting')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('person_id', models.UUIDField(help_text='person_id', default=uuid.uuid4, verbose_name='Person uuid')),
                ('person_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('speaker_id', models.UUIDField(help_text='speaker_id', default=uuid.uuid4, verbose_name='Speaker uuid')),
                ('speaker_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='meetingpersonrealtion',
            name='person',
            field=models.ForeignKey(to='Veeva_Meeting.Person'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='member',
            field=models.ManyToManyField(to='Veeva_Meeting.Person', through='Veeva_Meeting.MeetingPersonRealtion'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='speaker',
            field=models.OneToOneField(to='Veeva_Meeting.Speaker'),
        ),
    ]
