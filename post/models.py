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


        def get_create_url(self):
                return reverse('post_create')

        def get_delete_url(self):
                return reverse('post_delete', kwargs={'detail_id':self.id})

        def get_update_url(self):
                return reverse('post_update', kwargs={'detail_id':self.id })