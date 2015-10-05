# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0039_privacydocs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=2)),
                ('question_id', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=500)),
                ('option_a', models.CharField(max_length=200)),
                ('option_b', models.CharField(max_length=200)),
                ('option_c', models.CharField(max_length=200)),
                ('option_d', models.CharField(max_length=200)),
                ('option_correct', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'question',
            },
        ),
    ]
