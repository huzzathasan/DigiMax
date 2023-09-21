from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import format_html

# Create your models here.

class Category(models.Model):

    title = models.CharField(('Category Title'), max_length=255)

    def __str__(self):
        return self.title
    

class Post(models.Model):
    title = models.CharField(verbose_name="Post Title", max_length=255)
    category = models.ForeignKey(Category, verbose_name=("Post Category"), on_delete=models.CASCADE)
    img = models.ImageField(upload_to='post_img/', default='post_img/default_img.jpg')
    content = models.TextField(verbose_name=('Post Content'))
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, verbose_name=("Post Author"), on_delete=models.CASCADE, default=User)
    tag = models.CharField(('Post Tag'), max_length=255, blank=True, null=True, help_text='You Can Avoid This Field if Unnessery')
    url = models.SlugField((f'Post Url (Optional)'), blank=True, unique=True, help_text='This Field Automatic Generated based on post Category & Post Title. Also You can create Custom url.')

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = slugify(f'{self.category.title}-{self.title[0:5]}')
        return super().save(*args, **kwargs)
    
    def image(self):
        return format_html('<img src="/media/{}" style="width: 48px; height: 48px; object-fit: cover;" />'.format(self.img))

    def __str__(self):
        return self.title
    

class FeaturePost(models.Model):
    title = models.CharField(verbose_name="Post Title", max_length=255)
    category = models.ForeignKey(Category, verbose_name=("Post Category"), on_delete=models.CASCADE)
    img = models.ImageField(('Feature Post Image'), upload_to='post_img/feature_post', default='post_img/default_img.jpg')
    content = models.TextField(verbose_name=('Post Content'))
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, verbose_name=("Post Author"), on_delete=models.CASCADE, default=User)
    tag = models.CharField(('Post Tag'), max_length=255, blank=True, null=True, help_text='You Can Avoid This Field if Unnessery')
    url = models.SlugField((f'Post Url (Optional)'), blank=True, unique=True, help_text='This Field Automatic Generated based on post Category & Post Title. Also You can create Custom url.')

    class Meta:
        verbose_name = ("FeaturePost")
        verbose_name_plural = ("FeaturePosts")
        
    def image(self):
        return format_html('<img src="/media/{}" style="width: 48px; height: 48px; object-fit: cover;" />'.format(self.img))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("FeaturePost_detail", kwargs={"pk": self.url})

