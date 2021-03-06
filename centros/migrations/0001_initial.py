# Generated by Django 4.0.3 on 2022-03-14 09:49

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.IntegerField()),
                ('nombreCentro', models.CharField(help_text='Introduzca nombres del centro', max_length=250)),
                ('tipoCentro', models.CharField(help_text='Introduzca el tipo de centro', max_length=250)),
                ('naturaleza', models.CharField(max_length=250)),
                ('localidad', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=250)),
                ('codPostal', models.IntegerField()),
                ('long', models.DecimalField(decimal_places=8, max_digits=10)),
                ('lat', models.DecimalField(decimal_places=8, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'centros',
            },
        ),
        migrations.CreateModel(
            name='CentrosIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('introduccion', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
