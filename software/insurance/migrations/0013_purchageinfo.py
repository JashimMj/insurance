# Generated by Django 3.1.7 on 2021-03-27 05:59

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0012_auto_20210326_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pdate', models.DateField(blank=True, null=True)),
                ('Invoice_no', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Rate', models.IntegerField(blank=True, null=True)),
                ('Amount', models.IntegerField(blank=True, null=True)),
                ('Total', models.IntegerField(blank=True, null=True)),
                ('Vat', models.IntegerField(blank=True, null=True)),
                ('Sub_Total', models.IntegerField(blank=True, null=True)),
                ('Less', models.IntegerField(blank=True, null=True)),
                ('Grant_total', models.IntegerField(blank=True, null=True)),
                ('Item_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insurance.itementrym')),
                ('Supplier_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insurance.supplierinfom')),
            ],
            managers=[
                ('objests', django.db.models.manager.Manager()),
            ],
        ),
    ]