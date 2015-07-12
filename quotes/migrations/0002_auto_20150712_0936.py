# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='author_name',
            field=models.CharField(default=b'N/A', max_length=25),
        ),
        migrations.AddField(
            model_name='quote',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 12, 9, 36, 47, 604477, tzinfo=utc), verbose_name=b'date published', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quote',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
