# Generated by Django 3.1.7 on 2021-05-31 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0029_auto_20210530_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issueinfom',
            name='Rate',
        ),
    ]
