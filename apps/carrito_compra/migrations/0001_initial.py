# Generated by Django 4.1.5 on 2023-01-27 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('is_created', models.BooleanField(default=False)),
                ('subtotal', models.IntegerField(default=0)),
                ('descuento', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'api_carrito',
            },
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0)),
                ('descuento_total', models.FloatField(default=0)),
                ('cantidad_total', models.IntegerField(default=0)),
                ('carrito', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carrito_orden', to='carrito_compra.carrito')),
            ],
            options={
                'db_table': 'api_orden',
            },
        ),
    ]
