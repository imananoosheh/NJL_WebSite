import os

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models.signals import pre_save, pre_delete, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.conf import settings
from .validators import validate_file_extension_video

class sections(models.Model):
    title = models.CharField(max_length = 64, verbose_name="Title (Enlgish)")
    slug = models.SlugField(max_length=140, unique=True, null =True, editable= False)
    farsi_title = models.CharField(max_length = 64, verbose_name="Title (Farsi)")
    description = RichTextUploadingField(config_name='awesome_ckeditor',  verbose_name="Description (English)")
    farsi_description = RichTextUploadingField(config_name='awesome_ckeditor', verbose_name="Description (Farsi)")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Section"    
        verbose_name_plural = "Sections"    
    
    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while sections.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug


@receiver(pre_save, sender=sections, dispatch_uid='slugify')
def generateSlugC(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = instance._get_unique_slug()

class landingVideo(models.Model):
    vOp = models.FileField(upload_to='MPV/',verbose_name="Video", validators = [validate_file_extension_video])
    name = models.CharField(max_length = 64, verbose_name = "Name", null = True)
    class Meta:
        verbose_name = "video"
        verbose_name_plural = "video"
    def __str__(self):
        return str(self.name)


@receiver(models.signals.post_delete, sender=landingVideo)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.vOp:
        if os.path.isfile(instance.vOp.path):
            os.remove(instance.vOp.path)

@receiver(models.signals.pre_save, sender=landingVideo)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = landingVideo.objects.get(pk=instance.pk).vOp
    except landingVideo.DoesNotExist:
        return False

    new_file = instance.vOp
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
