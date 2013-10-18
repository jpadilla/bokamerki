from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class List(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    user = models.ForeignKey(User)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)

        return super(List, self).save(*args, **kwargs)
