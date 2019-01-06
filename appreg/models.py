import requests
from django.db import models


class WebApp(models.Model):
    app_url = models.URLField(
        max_length=200, verbose_name="The URL of the application"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created at"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="last modified"
    )
    title = models.CharField(
        max_length=250, blank=True,
        verbose_name="Title"
    )
    subtitle = models.CharField(
        max_length=500, blank=True,
        verbose_name="Subtitle"
    )
    author = models.CharField(
        max_length=250, blank=True,
        verbose_name="Creators of the Web App"
    )
    description = models.TextField(
        blank=True, verbose_name="Description"
    )
    purpose_en = models.TextField(
        blank=True, verbose_name="Purpose of the Web App"
    )
    git_url = models.URLField(
        max_length=200,
        verbose_name="The URL the applications code repository",
        blank=True
    )

    def __str__(self):
        if self.title:
            return "{}".format(self.title)
        else:
            return "{}".format(self.app_url)

    def save(self, *args, **kwargs):
        url = "{}project-info".format(self.app_url)
        try:
            r = requests.get(url)
        except Exception as e:
            print(e)
            r = None
        if r and r.headers['content-type'] == "application/json":
            metadata = r.json()
            self.title = metadata['title']
            self.subtitle = metadata['subtitle']
            self.author = metadata['author']
            self.description = metadata['description']
            self.purpose_en = metadata['purpose_en']
            self.git_url = metadata['github']
        super().save(*args, **kwargs)
