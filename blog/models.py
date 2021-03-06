from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

# CkEditor
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=500, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="blog/")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    content = RichTextField()

    class Meta:
        verbose_name_plural = "Post"

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:post", args=[self.slug])
