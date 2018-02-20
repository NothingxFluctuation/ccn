# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('text', models.CharField(max_length=2000)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('from_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='sent_messages')),
                ('to_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='recieved_messages')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
