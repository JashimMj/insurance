# Generated by Django 3.1.7 on 2021-05-19 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0026_purchageinfom_invoice_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchageinfom',
            old_name='Invoice_no',
            new_name='Invoice_nos',
        ),
    ]
