from django.db import models
from django.urls import reverse


class Post(models.Model):

        title = models.CharField(max_length = 120, verbose_name = "Baslık")
        content = models.TextField(verbose_name="İçerik")
        publishing_date = models.DateTimeField(verbose_name="Oluşturulma Tarihi", auto_now_add= True)


        def __str__(self):
                return self.title

        def get_absolute_url(self):
                return reverse('post_detail', kwargs={'detail_id':self.id} )