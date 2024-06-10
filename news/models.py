
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils import timezone
from hitcount.models import HitCount


# Create your models here.

# Publish manager uchun model
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=New.Status.Published)


# Kategoriya yaratish qismi uchun model
class Category(models.Model):
    name = models.CharField(max_length=50)
    view_home = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Menyu'

    def __str__(self):
        return self.name

    @property
    def news(self):
        news = New.object.filter(category__id=self.id).order_by('-date')[:3]
        if news:
            return news
        return []

    @property
    def sub_category(self):
        sub = SubCategory.objects.filter(category_id=self.id)
        if sub:
            return sub
        return None


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Kichik menyu'

    def __str__(self):
        return self.name


# Yangiliklar uchun postlar qismi bo'yicha model
class New (models.Model):
    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = 'PB', 'Published'

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    full_info = RichTextField()
    header_images = models.ImageField(default='news/images/news.jpg', upload_to='news/images', blank=True)
    category = models.ManyToManyField(Category, blank=False, related_name='category')
    sub_category = models.ManyToManyField(SubCategory, blank=True)
    # view_count = models.IntegerField(default=0)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # upload_to = 'news/image'

    # hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.Draft
    )
    object = models.Manager()  # Default manager
    published = PublishedManager()

    class Meta:
        verbose_name_plural = 'Postlar'
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.slug)])

    def get_absolute_url_admin(self):
        return reverse('admin_news_detail', args=[str(self.slug)])

    def get_absolute_url_admin_edit(self):
        return reverse('admin_news_update', args=[str(self.slug)])

    def __str__(self):
        return self.name


#Contact bo'limi uchun model
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=1500)

    def __str__(self):
        return self.email
