# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Elo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('elo', models.IntegerField(default=800)),
                ('player', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('winner_before_elo', models.IntegerField()),
                ('winner_after_elo', models.IntegerField()),
                ('loser_before_elo', models.IntegerField()),
                ('loser_after_elo', models.IntegerField()),
                ('match_date', models.DateTimeField(verbose_name='match date')),
                ('loser', models.ForeignKey(related_name='loser', to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(related_name='winner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
