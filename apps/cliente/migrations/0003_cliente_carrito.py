# Generated by Django 4.1.5 on 2023-01-27 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrito_compra', '0004_alter_carrito_options_alter_orden_options_and_more'),
        ('cliente', '0002_remove_cliente_carrito'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='carrito',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carrito', to='carrito_compra.carrito'),
        ),
    ]
