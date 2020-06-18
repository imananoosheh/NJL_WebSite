from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from .validators import validate_file_extension_coverImage

class category(models.Model):
    name = models.CharField(max_length = 64, verbose_name = "Name (English)")
    farsiName = models.CharField(max_length = 64, verbose_name = "Name (Farsi)")
    slug = models.SlugField(max_length=140, unique=True, null =True, editable= False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while category.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

class article(models.Model):
    title = models.CharField(max_length = 64, null = True, verbose_name="Title (English)")
    slug = models.SlugField(max_length=140, unique=True, null =True, editable= False)
    farsiTitle = models.CharField(max_length = 64, null = True, verbose_name="Title (Farsi)")
    shortDescription = models.TextField(max_length = 400, null = True, verbose_name="Short Description (English)")
    farsiShortDescription = models.TextField(max_length = 400, null = True, verbose_name="Short Description (Farsi)")
    articleImage = models.ImageField( upload_to='news/', verbose_name="Cover Photo", validators = [validate_file_extension_coverImage])
    description = RichTextUploadingField(config_name='awesome_ckeditor', null = True, verbose_name="Description (English)")
    farsiDescription = RichTextUploadingField(config_name='awesome_ckeditor', null = True, verbose_name="Description (Farsi)")
    category = models.ManyToManyField(category, verbose_name="Categories")
    date = models.CharField(max_length = 64, null = True, verbose_name="Date")
    Farsidate = models.CharField(max_length = 64, null = True, verbose_name="Jalali Date")
    authorName = models.CharField(max_length = 64, null = True, verbose_name="Author Name (English)")
    farsiAuthoName = models.CharField(max_length = 64, null = True, verbose_name="Author Name (Farsi)")
    def __str__(self):
        return self.title
    
    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while article.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
    def get_absolute_url(self):
        return reverse("news:detail" , kwargs={"slug" : self.slug})
        #return "/posts/%s/" %(self.slug)
    class Meta:
        verbose_name_plural = "Article"


@receiver(pre_save, sender=category, dispatch_uid='slugify1')
def generateSlugC(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = instance._get_unique_slug()

@receiver(pre_save, sender=article, dispatch_uid='slugify2')
def generateSlugA(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = instance._get_unique_slug()
