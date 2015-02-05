#from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models

class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    list_display = ("email", "created")
 #   prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Entry, EntryAdmin)