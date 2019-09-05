from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    relations = models.ManyToManyField('Section', through='Tags')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Section(models.Model):

    name = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        ordering = ['name']
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class Tags(models.Model):

    article = models.ForeignKey(Article,  on_delete=models.CASCADE, related_name='tags')
    section = models.ForeignKey(Section,  on_delete=models.CASCADE, verbose_name='Раздел')
    main = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        verbose_name_plural = 'Тематики статьи'
