# Generated by Django 4.1.5 on 2023-01-27 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='carrito',
        ),
    ]
