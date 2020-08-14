from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):

    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ('content')


admin.site.register(models.Post, PostAdmin)

admin.site.register(models.Profile)

admin.site.register(models.Comment)
