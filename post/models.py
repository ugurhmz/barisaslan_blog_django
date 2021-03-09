from django.db import models
from django.urls import reverse
from django.utils.text import  slugify


class Post(models.Model):

        title = models.CharField(max_length = 120, verbose_name = "Baslık")
        content = models.TextField(verbose_name="İçerik")
        publishing_date = models.DateTimeField(verbose_name="Oluşturulma Tarihi", auto_now_add= True)
        image = models.ImageField(blank = True, null= True)
        slug = models.SlugField(max_length = 130,unique =True, editable=False)

        def __str__(self):
                return self.title

        def get_absolute_url(self):
                return reverse('post_detail', kwargs={'slug':self.slug} )


        def get_create_url(self):
                return reverse('post_create')

        def get_delete_url(self):
                return reverse('post_delete', kwargs={'slug':self.slug})

        def get_update_url(self):
                return reverse('post_update', kwargs={'slug':self.slug })


        def get_unique_slug(self):
                slug = slugify(self.title.replace('ı','i'))
                unique_slug = slug
                counter =1
                while Post.objects.filter(slug=unique_slug).exists():
                        unique_slug = "{}-{}".format(slug, counter)
                        counter += 1
                return  unique_slug



        def save(self, *args, **kwargs):

                self.slug = self.get_unique_slug()

                return super(Post,self).save(*args,**kwargs)






        class Meta:
                ordering=['-publishing_date','id']