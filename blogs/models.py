from pydoc import classname
from django.db import models

# Create your models here.

class Post(models.Model):
    name=models.CharField(max_length=250)
    detail=models.TextField(blank=True,null=True)
    published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name