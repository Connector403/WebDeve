# Generated by Django 2.1 on 2020-05-03 21:42

from django.db import migrations


def capitalize(apps, schema_editor):
    Product = apps.get_model('main', 'Product')
    for product in Product.objects.all():
        product.name = product.name.capitalize()
        product.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_productimage_thumbnail'),
    ]

    operations = [
    ]