# Generated by Django 3.1.7 on 2021-03-27 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0014_auto_20210327_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchageinfo',
            name='Item_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
