# Generated by Django 4.1 on 2022-08-18 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paid_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]