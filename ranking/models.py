from re import template
from django.db import models

# Create your models here.

from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

# Create your models here.
class RankingPage(Page):
    introduccion = RichTextField(blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

