# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('loginName', models.CharField(default=b'', max_length=64)),
                ('password', models.CharField(default=b'', max_length=64)),
                ('realName', models.CharField(default=b'', max_length=64, blank=True)),
                ('isDisabled', models.BooleanField()),
                ('creater', models.CharField(default=b'', max_length=64)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
