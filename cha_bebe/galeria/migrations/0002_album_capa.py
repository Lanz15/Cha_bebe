# Generated by Django 3.0.6 on 2020-05-14 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='capa',
            field=models.ImageField(blank=True, null=True, upload_to='galeria/capa'),
        ),
    ]