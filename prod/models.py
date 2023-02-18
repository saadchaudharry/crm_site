from django.db import models
from hypersite.utils import unique_slug_generator
from django.db.models.signals import pre_save
# Create your models here.

class products(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=999)
    modelNO = models.CharField(max_length=999)
    Enable = models.BooleanField(default=True)
    index  = models.BooleanField()
    position  =models.IntegerField(blank=True, null=True,unique=True)

    description = models.TextField(max_length=12000)
    document =models.FileField(upload_to="document/",blank=True, null=True)
    note  = models.CharField(max_length=999, blank=True, null=True)
    htmlcode = models.TextField(max_length=12000, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.title)

def prodsignal(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(prodsignal,sender=products)
