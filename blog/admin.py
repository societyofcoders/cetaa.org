from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created","status")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("title", "uid", "post_id" ,"vote")

class PostLabelAdmin(admin.ModelAdmin):
    list_display = ("post_id", "label_id")

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment,CommentAdmin)
admin.site.register(models.Label)
admin.site.register(models.PostLabels,PostLabelAdmin)
