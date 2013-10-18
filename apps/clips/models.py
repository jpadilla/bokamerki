from django.db import models
from django.contrib.auth.models import User

class Clip(models.Model):
    title = models.CharField(blank=True, max_length=255)
    url = models.URLField()
    user = models.ForeignKey(User)
    list = models.ForeignKey('lists.List')
    notes = models.TextField(blank=True)
    comments = models.ManyToManyField('comments.Comment', blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    favicon_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.url
