# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default=b'', max_length=64)),
                ('sort', models.IntegerField(default=0)),
                ('isDisabled', models.BooleanField()),
                ('cid', models.CharField(max_length=64)),
                ('pid', models.CharField(max_length=64)),
                ('creater', models.CharField(default=b'', max_length=64)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default=b'', max_length=64)),
                ('linkSrc', models.CharField(default=b'', max_length=200)),
                ('pirce', models.FloatField()),
                ('sort', models.IntegerField(default=0)),
                ('isDisabled', models.BooleanField()),
                ('categoryId', models.CharField(max_length=64)),
                ('creater', models.CharField(default=b'', max_length=64)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
