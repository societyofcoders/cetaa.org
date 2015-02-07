from django.contrib import admin
from . import models

class CommentAdmin(admin.ModelAdmin):
    list_display = ("title", "uid", "post_id" ,"vote")

class PostLabelAdmin(admin.ModelAdmin):
    list_display = ("post_id", "label_id")

class LabelInline(admin.TabularInline):
	model = models.PostLabels
	extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created","status")
    inlines = [LabelInline]

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment,CommentAdmin)
admin.site.register(models.Label)
admin.site.register(models.PostLabels,PostLabelAdmin)
