from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# Create your models here.

class Biblemodel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=30)
    good = models.IntegerField(null=True, blank=True,default=0)
    goodtext = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    url = models.URLField(max_length = 300, blank = True)
    category = models.CharField(max_length=10)
    sex = models.CharField(max_length = 10)
    age = models.CharField(max_length = 10)

    class Meta:
        ordering = ['-created_date']

    def publish(self):
        self.published_date = timezone.now()
        self.save()



