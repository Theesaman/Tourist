from django.contrib import admin
from .models import Contact, Team, Service, Packages
from django.utils.html import format_html

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["first_name", "email"]
# Register your models here.
admin.site.register((Service))

@admin.register(Packages)
class PackagetAdmin(admin.ModelAdmin):
    list_display = ["person", "money"]

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('full_name','image')

    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
