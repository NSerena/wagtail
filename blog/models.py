from django.db import models
from django import forms

from pelis.models import Pelicula

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel,  MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


from wagtail.search import index


class BlogIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)

        categoria = request.GET.get('categoria')
        
        qs = ''

        if categoria == 'viajes':
            entradas = ViajesPage.objects.live().order_by('-first_published_at')
        elif categoria == 'peliculas':
            entradas = PeliculaPage.objects.live().order_by('-first_published_at')
        elif categoria == 'deportes':
            entradas = DeportePage.objects.live().order_by('-first_published_at')
        elif categoria == 'posts':
            entradas = BlogPage.objects.live().order_by('-first_published_at')
        else:
            entradas = self.get_children().live().order_by('-first_published_at')

        context['blogpages'] = entradas

        return context

    parent_page_types = ['wagtailcore.Page']
    subpage_types = ['BlogPage', 'ViajesPage', 'DeportePage','PeliculaPage']



# Tags del Blog
class BlogTagIndexPage(Page):
    
    subpage_types = []
    
    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )






# Modelo P??gina Blog
class BlogPage(Page):
    date = models.DateField("Fecha Post")
    intro = models.CharField("Introducci??n", max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)


    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
            ],
            heading='Informaci??n'
        ),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', 
            label="Galer??a de im??genes"),
    ]

    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []


# Modelo P??gina Viajes
class ViajesPage(Page):
    lugar = models.CharField(max_length=30)
    date = models.DateField("Fecha Viaje", blank=True, null=True)
    intro = models.CharField("Introducci??n", max_length=250, blank=True, null=True)
    body = RichTextField(blank=True)
    coord = models.CharField(blank=True, max_length=20)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)
    imagen = models.URLField(blank=True)


    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
            ],
            heading='Informaci??n'
        ),
        FieldPanel('lugar'),
        FieldPanel('coord'),
        FieldPanel('intro'),
        FieldPanel('imagen'),
        FieldPanel('body', classname="full"),

    ]

    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []


# Modelo P??gina peli
class PeliculaPage(Page):
    lugar = models.CharField(max_length=30)
    intro = models.CharField("Introducci??n", max_length=250, blank=True, null=True)
    body = RichTextField(blank=True)
    imagen = models.URLField(blank=True)

    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
            ],
            heading='Informaci??n'
        ),
        FieldPanel('lugar'),
        FieldPanel('intro'),
        FieldPanel('imagen'),
        FieldPanel('body', classname="full"),

    ]

    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []
   

class DeportePage(Page):
    lugar = models.CharField(max_length=30)
    intro = models.CharField("Introducci??n", max_length=250, blank=True, null=True)
    body = RichTextField(blank=True)
    imagen = models.URLField(blank=True)

    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
            ],
            heading='Informaci??n'
        ),
        FieldPanel('lugar'),
        FieldPanel('intro'),
        FieldPanel('imagen'),
        FieldPanel('body', classname="full"),

    ]

    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []

    

class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, 
        on_delete=models.CASCADE, 
        related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]





@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categor??as de blog'
        verbose_name = 'categor??a de blog'



