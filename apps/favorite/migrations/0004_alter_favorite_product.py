# Generated by Django 4.0.4 on 2022-07-20 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_initial'),
        ('favorite', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_prod', to='product.product', unique=True),
        ),
    ]
