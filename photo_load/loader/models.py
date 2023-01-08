from django.db import models



class Photo(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Картинка')

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"
