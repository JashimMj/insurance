# Generated by Django 3.1.7 on 2021-03-24 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0004_remove_userprofilem_country_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemEntryM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Itemname', models.CharField(blank=True, max_length=255, null=True)),
                ('unit', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
