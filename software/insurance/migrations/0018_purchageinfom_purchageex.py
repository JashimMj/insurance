# Generated by Django 3.1.7 on 2021-03-27 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0017_auto_20210327_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchageinfom',
            name='purchageEx',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insurance.purchageextendm'),
        ),
    ]
