from django.contrib import admin
from .models import Gamer, Videogame, Party
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class GamerAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "steam")
    exclude = (
        'groups',
        'last_login',
        'is_superuser',
        'is_staff',
        'date_joined',
        'first_name',
        'last_name',
        'is_active',
        'user_permissions'
    )


admin.site.register(Gamer, GamerAdmin)
