# Generated by Django 2.2.26 on 2022-01-08 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Imagen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=4000)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Imagen.Imagen')),
            ],
        ),
    ]