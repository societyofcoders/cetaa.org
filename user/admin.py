from django.contrib import admin
from user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("fname","lname","passyear","dept","verification")

admin.site.register(User,UserAdmin)
