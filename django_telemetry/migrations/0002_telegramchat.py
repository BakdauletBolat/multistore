# Generated by Django 4.1.2 on 2022-10-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_telemetry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(max_length=255)),
            ],
        ),
    ]