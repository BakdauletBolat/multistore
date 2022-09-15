# Generated by Django 4.0.7 on 2022-09-13 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('busket', '0002_busket_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='busketitem',
            name='new_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='busketitem',
            name='price',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='busketitem',
            name='sales',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='busketitem',
            name='busket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='busket.busket'),
        ),
    ]
