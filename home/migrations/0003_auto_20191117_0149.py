# Generated by Django 2.2.4 on 2019-11-17 09:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20191117_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 9, 49, 50, 978773, tzinfo=utc)),
        ),
    ]