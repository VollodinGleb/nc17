from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor_uploader.fields import RichTextUploadingField
from phonenumber_field.modelfields import PhoneNumberField
from adminsortable.models import SortableMixin


class Constants:
    LANGUAGE_EN, LANGUAGE_RU, LANGUAGE_UA = 0, 1, 2
    LANGUAGE_CHOICES = (
        (LANGUAGE_EN, 'en'),
        (LANGUAGE_RU, 'ru'),
        (LANGUAGE_UA, 'uk')
    )
    LANGUAGE_CODES = {
        'en': LANGUAGE_EN,
        'ru': LANGUAGE_RU,
        'uk': LANGUAGE_UA
    }


class Photo(SortableMixin):
    name = models.CharField(max_length=100, help_text='Название для фото')
    image = ThumbnailerImageField(help_text='собственно, фотка')
    description = models.TextField(help_text='описание для галереи, когда кликаешь на картинку')

    order_id = models.PositiveIntegerField(help_text='Порядковый номер',
                                           default=0,
                                           editable=False,
                                           db_index=True)

    class Meta:
        ordering = ['order_id']

    def __str__(self):
        return self.name


class Video(SortableMixin):
    name = models.CharField(max_length=100, help_text='Название для видео')
    link = models.URLField(help_text='Ссылка на видео(youtube/etc)')
    order_id = models.PositiveIntegerField(help_text='Порядковый номер',
                                           default=0,
                                           editable=False,
                                           db_index=True)
    show_in_photos = models.BooleanField(help_text='Отражать в фото галерее', default=False)

    class Meta:
        ordering = ['order_id']

    def __str__(self):
        return self.name


class About(models.Model):
    text = RichTextUploadingField(help_text='Содержание текста')
    language = models.IntegerField(help_text='язык',
                                   choices=Constants.LANGUAGE_CHOICES,
                                   default=Constants.LANGUAGE_EN)

    def __str__(self):
        return Constants.LANGUAGE_CHOICES[self.language][1] + ' about'


class SectionImage(models.Model):
    name = models.CharField(max_length=100, help_text='Название картинки для админки')
    image = ThumbnailerImageField()
    section_text = models.ForeignKey('Section', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SectionVideo(models.Model):
    name = models.CharField(max_length=100, help_text='Название вилео для админки')
    link = models.URLField(help_text='Ссылка на видео')
    section_text = models.ForeignKey('Section', on_delete=models.CASCADE)
    youtube_video_id = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if '/' in self.link:
            self.youtube_video_id = self.link.split('/')[-1]
        super().save(*args, **kwargs)


class Section(models.Model):
    class Meta:
        verbose_name = "Cекция лэндинга"
        verbose_name_plural = "Секции лэндинга"

    name = models.CharField(max_length=100, help_text='Название секции(НЕ ТРОГАТЬ)')
    heading = models.CharField(max_length=100, help_text='Заголовок')
    button_text = models.CharField(max_length=100, help_text='Текст кнопки', blank=True, null=True)
    text = RichTextUploadingField(help_text='Текст английский', blank=True, null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100, help_text='Имя')
    email = models.EmailField(help_text='почта')
    phone_number = PhoneNumberField(help_text='Номер')
    text = models.TextField(help_text='Текст сообщения')

    def __str__(self):
        return self.name


class Promotion(models.Model):
    name = models.CharField(max_length=100, help_text="Название. Отражается в ссылке на текст и админке."
                                                      "ТОЛЬКО КИРИЛЛИЦА, без пробелов!!!")
    text_en = RichTextUploadingField(help_text="Содержание текста английское.")
    text_ru = RichTextUploadingField(help_text="Содержание текста русское.")
    text_ua = RichTextUploadingField(help_text="Содержание текста украинское.")

    slug = models.SlugField(help_text='Строка для ссылки на текст. Не менять руками!')

    def __str__(self):
        return self.name


