# Generated by Django 4.0.7 on 2022-09-02 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beav', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attribute',
            options={'verbose_name': 'Аттрибут', 'verbose_name_plural': 'Аттрибуты'},
        ),
        migrations.AlterModelOptions(
            name='entity',
            options={'verbose_name': 'Сущность', 'verbose_name_plural': 'Сущности'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterModelOptions(
            name='value',
            options={'verbose_name': 'Поля', 'verbose_name_plural': 'Поля'},
        ),
    ]