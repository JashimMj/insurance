# Generated by Django 3.1.7 on 2021-03-26 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0010_employeesinformationm'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeesinformationm',
            name='Email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employeesinformationm',
            name='Phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]