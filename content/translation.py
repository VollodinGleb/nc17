from modeltranslation.translator import translator, TranslationOptions
from .models import Section


class SectionTranslationOptions(TranslationOptions):
    fields = ('heading', 'button_text', 'text')


translator.register(Section, SectionTranslationOptions)

