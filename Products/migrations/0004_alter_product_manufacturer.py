# Generated by Django 4.2.6 on 2023-10-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
