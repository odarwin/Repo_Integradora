# Generated by Django 2.2.26 on 2022-01-20 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Prediccion', '0003_prediccion_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prediccion',
            old_name='estado',
            new_name='state',
        ),
    ]
