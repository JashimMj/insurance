# Generated by Django 3.1.7 on 2021-03-26 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0011_auto_20210326_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeesinformationm',
            name='Email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
    ]