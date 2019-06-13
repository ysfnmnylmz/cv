from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Post Title')
    image = models.ImageField(verbose_name='Image', default='')
    contenttext = models.TextField(verbose_name='Post Content')
    publishdate = models.DateField()

    class Meta:
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'
        ordering = ['publishdate']

    def __str__(self):
        return self.title
