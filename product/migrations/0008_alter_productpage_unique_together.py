# Generated by Django 4.1.1 on 2022-11-03 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0004_language_photo'),
        ('store', '0002_alter_store_city'),
        ('product', '0007_alter_productpage_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productpage',
            unique_together={('lang', 'store', 'product', 'city')},
        ),
    ]