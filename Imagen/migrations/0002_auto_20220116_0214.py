# Generated by Django 2.2.26 on 2022-01-16 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Imagen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='description',
            field=models.TextField(default='', max_length=4000),
        ),
    ]