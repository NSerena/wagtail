from re import template
from django.db import models

# Create your models here.

from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your models here.





# Modelo de página de deportistas
class RankingPage(Page):
    introduccion = RichTextField(blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

