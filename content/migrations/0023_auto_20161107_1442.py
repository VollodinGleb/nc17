# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 14:42
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0022_auto_20161107_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Содержание текста'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='text_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Содержание текста английское.'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='text_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Содержание текста русское.'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='text_ua',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Содержание текста украинское.'),
        ),
        migrations.AlterField(
            model_name='section',
            name='text_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Текст английский'),
        ),
        migrations.AlterField(
            model_name='section',
            name='text_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Текст русский'),
        ),
        migrations.AlterField(
            model_name='section',
            name='text_ua',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Текст украинский'),
        ),
    ]
