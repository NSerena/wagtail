from pyexpat import model
from django.db import models
from django import forms

from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your models here.

## Page que mostrará el index de las películas
## Hereda solo de Home y no descendientes

## Modelo para Centros



class Centro(models.Model):
    objectid = models.IntegerField()
    nombreCentro = models.CharField(max_length = 250, help_text='Introduzca nombres del centro')
    tipoCentro = models.CharField(max_length = 250, help_text='Introduzca el tipo de centro')
    naturaleza = models.CharField(max_length = 250)
    localidad = models.CharField(max_length = 250)
    direccion = models.CharField(max_length = 250)
    codpostal = models.CharField(max_length = 250)
    long = models.DecimalField(max_digits=10, decimal_places=8)
    lat = models.DecimalField(max_digits=10, decimal_places=8)

    
    panels = [
        FieldPanel('objectid'),
        FieldPanel('nombreCentro'),
        FieldPanel('tipoCentro'),
        FieldPanel('naturaleza'),
        FieldPanel('localidad'),
        FieldPanel('direccion'),
        FieldPanel('codpostal'),
        FieldPanel('long'),
        FieldPanel('lat')
    ]
    def __str__(self):
        return f'{self.nombreCentro} ({self.tipoCentro})'
    
    class Meta:
        verbose_name_plural = 'centros'
    

class CentrosIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]


    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        context['centros'] = Centro.objects.all()
        
        return context

    def paginate(self, request, *args):
        page = request.GET.get('page')
        paginator = Paginator(self.get_centros(), 12)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages
    subpage_types = []
    
