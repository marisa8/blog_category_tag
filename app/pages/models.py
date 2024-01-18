from django.db import models


class Category(models.Model):
    name = models.CharField('category name', max_length=255)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('tag name', max_length=50)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField('title', max_length=100)
    text = models.TextField('text')
    category = models.ForeignKey(Category, verbose_name='category', on_delete=models.PROTECT)
    tag = models.ManyToManyField(Tag, verbose_name='tag')
    relation = models.ManyToManyField('self', verbose_name='relation', blank=True, null=True)
    created_at = models.DateTimeField('created date', auto_now_add=True)
    updated_at = models.DateTimeField('updated date', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
