# Generated by Django 4.0.7 on 2022-09-02 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='store',
            options={'verbose_name': 'Магазин', 'verbose_name_plural': 'Магазины'},
        ),
    ]