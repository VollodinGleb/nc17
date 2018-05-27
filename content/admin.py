from django.contrib import admin
from .models import Photo, Video, About, Contact, Section, Promotion, SectionImage, SectionVideo
from adminsortable.admin import SortableAdmin
from modeltranslation.admin import TranslationAdmin


admin.site.register((About, Contact))
admin.site.register(Photo, SortableAdmin)
admin.site.register(Video, SortableAdmin)


class InlineSectionImageAdmin(admin.TabularInline):
    model = SectionImage
    fields = ('name', 'image')
    extra = 1
    classes = ('collapse',)


class InlineSectionVideoAdmin(admin.TabularInline):
    model = SectionVideo
    fields = ('name', 'link')
    extra = 1
    classes = ('collapse',)


class SectionAdmin(TranslationAdmin):
    fieldsets = (
        ('Name', {
            'fields': ('name',),
            'classes': ('collapse',)
        }),
        ('Headings', {
            'fields': ('heading',),
            'classes': ('collapse',)
        }),
        ('Button texts', {
            'fields': ('button_text',),
            'classes': ('collapse',)
        }),
        ('Texts', {
            'fields': ('text',),
            'classes': ('collapse',)
        }),
    )
    inlines = (InlineSectionImageAdmin, InlineSectionVideoAdmin)


admin.site.register(Section, SectionAdmin)


class PromotionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Promotion, PromotionAdmin)
