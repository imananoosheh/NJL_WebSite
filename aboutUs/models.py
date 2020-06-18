from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

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


