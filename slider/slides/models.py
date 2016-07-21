from django.db import models
from django_resized import ResizedImageField


class Slide(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name="Заголовок слайда",
        blank=True,
        null=True)
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True)
    image = ResizedImageField(
        size=[1134, 455],
        crop=['middle', 'center'],
        quality=100,
        upload_to="slides",
        verbose_name="Картинка")
    right = models.BooleanField(
        default=False,
        verbose_name="Подпись справа")

    def __str__(self):
        return "Слайд №%s" % self.id

    class Meta:
        abstract = True
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды на главной"

