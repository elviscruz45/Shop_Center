# Generated by Django 4.1 on 2022-09-03 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requestt',
            options={'ordering': ['id'], 'verbose_name': 'request', 'verbose_name_plural': 'requests'},
        ),
        migrations.AlterModelTable(
            name='requestt',
            table='request',
        ),
    ]
