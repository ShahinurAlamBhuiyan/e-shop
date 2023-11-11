from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',) # ordering span name
        verbose_name_plural = 'Categories'  # collection name spell

    def __str__(self): # visualize items correctly to the admin dash 
        return self.name

