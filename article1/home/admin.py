from django.contrib import admin
from.models import Article

# Register your models here.
@admin.register(Article)
class Adminarticle(admin.ModelAdmin):
    list_display=['name','descriptions']
    # link_list_display=['descriptions']

    