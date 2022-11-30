from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish"),
    (2, "Delete"),
)


class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    cover = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title
