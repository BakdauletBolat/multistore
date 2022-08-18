# Generated by Django 4.1 on 2022-08-18 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('handbook', '0001_initial'),
        ('product', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='handbook.category')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='handbook.city')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='product.product')),
                ('quality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='handbook.quality')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='store.store')),
                ('wirehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='handbook.wirehouse')),
            ],
        ),
    ]
