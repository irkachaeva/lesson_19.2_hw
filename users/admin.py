from django.contrib import admin
from users.models import User
from django.contrib.auth.models import Group

# Register your models here.
#admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email")



