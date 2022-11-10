from django.db import models

# Create your models here   .
class Post(models.Model):
    title = models.CharField(max_length=255)
    # text field with constrains in length
    content = models.TextField()
    # text field without constrains in length
    published = models.BooleanField(default=False)
    # true/false flag
    created = models.DateTimeField(auto_now_add=True)
    # data utworzenia - tylko przy utworzeniu
    modified = models.DateTimeField(auto_now=True)