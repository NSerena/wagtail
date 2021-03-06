# Generated by Django 3.2.11 on 2022-02-22 09:00

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('blog', '0012_delete_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Viajes',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('lugar', models.CharField(max_length=40)),
                ('fecha', models.DateField(verbose_name='Fecha del Viaje')),
                ('body', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
