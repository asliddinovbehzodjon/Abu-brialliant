# Generated by Django 4.0.4 on 2022-04-21 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customer_order_alter_category_options_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='adress',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zipcode',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
