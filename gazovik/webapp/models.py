from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from transliterate import translit, get_available_language_codes
from django.template.defaultfilters import slugify


class Tovar(models.Model):
    """docstring for Tovar."""
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    name = models.CharField(blank=False, max_length=100)
    description = models.TextField(blank=True, max_length=100)
    image = models.ImageField(upload_to="upload/images/", blank=True)
    # height_field=640, width_field=360,
    image_mini = models.ImageField(upload_to="upload/images/thumb/", blank=True)
    price = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey('Category', db_index=True)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str('[{}] {}').format(self.name, self.description)

    def save(self):
        if not self.slug:
            self.slug = slugify(translit(self.name, 'ru', reversed=True))
        super(Tovar, self).save()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    # def get_absolute_url(self):
    #     return reverse('webapp_tovar_detail', args=(self.slug,))


class Category(models.Model):
    """docstring for Category."""
    name = models.CharField(blank=False, max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return str('[{}] {}').format(self.name, self.slug)
