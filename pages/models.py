from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name="Название", max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):
    file = models.FileField(verbose_name='Файл', upload_to="database/files", blank=True)
    title = models.CharField(verbose_name="Название", max_length=200)
    description = models.TextField(verbose_name="Описание", blank=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.PROTECT, related_name="projects")
    github_link = models.URLField(verbose_name="Ссылка на гитхаб", blank=True)
    website_link = models.URLField(verbose_name="Ссылка на сайт", blank=True)


class Image(models.Model):
    image = models.ImageField(verbose_name='Фото', upload_to="database/images")
    project = models.ForeignKey(Project, related_name="images", on_delete=models.PROTECT)
