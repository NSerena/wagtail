# Generated by Django 3.2.11 on 2022-02-28 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_viajespage_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicapage',
            name='imagen',
            field=models.URLField(blank=True),
        ),
    ]
