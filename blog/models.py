from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

STATUS = (
    (0, "Draft"),
    (1, "Publish"),
    (2, "Delete"),
)


class BlogPost(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    cover = models.ImageField(upload_to='images/', null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True, auto_created=True, null=False, blank=False)
    # published_on = models.DateTimeField(null=True)
    # updated_on = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.title
