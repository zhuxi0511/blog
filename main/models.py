from django.db import models
from markdownx.models import MarkdownxField

#from django_markdown.models import MarkdownField

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=30)
    #content = models.TextField()
    content = MarkdownxField()
    date = models.DateTimeField()
    is_show = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class AboutContent(models.Model):
    content = MarkdownxField()

    def __str__(self):
        return "about content"
