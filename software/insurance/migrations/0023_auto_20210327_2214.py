# Generated by Django 3.1.7 on 2021-03-27 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0022_auto_20210327_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchageinfom',
            name='Invoice_no',
        ),
        migrations.RemoveField(
            model_name='purchageinfom',
            name='Less',
        ),
        migrations.RemoveField(
            model_name='purchageinfom',
            name='Pdate',
        ),
        migrations.RemoveField(
            model_name='purchageinfom',
            name='Supplier_name',
        ),
        migrations.RemoveField(
            model_name='purchageinfom',
            name='Vat',
        ),
        migrations.AddField(
            model_name='purchageinfom',
            name='pex',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insurance.purchageextendm'),
        ),
    ]
