# Generated by Django 4.0 on 2021-12-15 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arabot', '0002_customer_procedure_customer_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedure',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]