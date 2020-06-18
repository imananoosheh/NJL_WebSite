from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from .validators import validate_recourse_file
from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save
import os
# Create your models here.

class recourse(models.Model):
    name = models.CharField(max_length = 64, verbose_name = "Name", null = True)
    File = models.FileField(verbose_name = "File", null = True, validators = [validate_recourse_file])
    def __str__(self):
         return self.name
    class Meta:
        verbose_name = "recourse"
        verbose_name_plural = "recourses"

class content(models.Model):
    title = models.CharField(max_length = 64, verbose_name="Title (English)")
    farsi_title = models.CharField(max_length = 64, verbose_name="Title (Farsi)")
    description = RichTextUploadingField(config_name='awesome_ckeditor', verbose_name="Description (English)")
    farsi_description = RichTextUploadingField(config_name='awesome_ckeditor', verbose_name="Description (Farsi)")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name ="Content"
        verbose_name_plural ="Content"

@receiver(post_delete, sender=recourse, dispatch_uid='clean')
def clean(sender,instance, **kwargs):
    if instance.File:
        if os.path.isfile(instance.File.path):
            os.remove(instance.File.path)


@receiver(pre_save, sender=recourse, dispatch_uid='address')
def fill_address(sender, instance, **kwargs):
    instance.address = "https://njl.institute/" + instance.File.url

