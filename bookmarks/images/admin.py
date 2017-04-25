from django.contrib import admin
from .models import Image

class ImageAdmin(admin.ModelAdmin):
    list_dispaly = ['title', 'slug', 'image', 'created']
    list_filter = ['created']

admin.site.register(Image, ImageAdmin)
