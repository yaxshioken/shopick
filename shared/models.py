from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugStampedModel(TimeStampedModel):
    slug = models.SlugField(unique=True)

    class Meta:
        abstract = True
