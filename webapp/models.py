from django.db import models

class Tovar(models.Model):
    """docstring for Tovar."""
    name = models.CharField('Tovar name', max_length=100)
    description = models.TextField('Description')
    image = models.Image
    price = models.IntegerField()
    category = models.ForeignKey('Category', db_index=True)
    date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return str('[{}] {} - {}').format(self.name, self.description, self.imagefield, self.price, self.category)

class Category(object):
    """docstring for Category."""
    name = models.CharField('category', max_length=100)
    slug = models.CharField()


    def __str__(self):
        return str('[{}] {}').format(self.name, self.slug)
