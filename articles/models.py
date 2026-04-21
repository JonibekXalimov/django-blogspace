from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django_ckeditor_5.fields import CKEditor5Field

class Article(models.Model):
    CATEGORY_CHOICES = (
        ("uzbekiston", "O'zbekiston"),
        ("jahon", "Jahon"),
        ("iqtisodiyot", "Iqtisodiyot"),
        ("sport", "Sport"),
        ("texnologiya", "Texnologiya"),
    )

    title = models.CharField(max_length=150)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default="uzbekiston")
    summary = models.CharField(max_length=150, blank=True)
    body = CKEditor5Field()
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

def get_absolute_url(self):
    return reverse("article_detail", args=[str(self.id)])

class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comments = models.CharField(max_length=150)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.comments
    
    def get_absolute_url(self):
        return reverse('list')
    
