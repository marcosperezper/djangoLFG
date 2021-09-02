from django.contrib import admin, messages
from .models import Gamer, Videogame, Party, Message
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class GamerAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "steam", "is_active")
    exclude = (
        'groups',
        'last_login',
        'is_superuser',
        'is_staff',
        'date_joined',
        'first_name',
        'last_name',
        'user_permissions'
    )

    actions = ['make_active', 'make_inactive']

    @admin.action(description="Mark as active")
    def make_active(self, request, queryset):
        queryset.update(is_active=1)
        messages.success(request, "Selected Gamer(s) Marked as Active Successfully !!")

    @admin.action(description="Mark as inactive")
    def make_inactive(self, request, queryset):
        queryset.update(is_active=0)
        messages.success(request, "Selected Gamer(s) Marked as Inactive Successfully !!")


class VideogameAdmin(admin.ModelAdmin):
    list_display = ("title", "genre")
    actions = ['make_active', 'make_inactive']

    @admin.action(description="Mark as active")
    def make_active(self, request, queryset):
        queryset.update(active=1)
        messages.success(request, "Selected Videogame(s) Marked as Active Successfully !!")

    @admin.action(description="Mark as inactive")
    def make_inactive(self, request, queryset):
        queryset.update(active=0)
        messages.success(
            request, "Selected Videogame(s) Marked as Inactive Successfully !!"
        )


class PartyAdmin(admin.ModelAdmin):
    list_display = ("name", "creator")
    actions = ['make_active', 'make_inactive']

    @admin.action(description="Mark as active")
    def make_active(self, request, queryset):
        queryset.update(active=1)
        messages.success(request, "Selected Party(ies) Marked as Active Successfully !!")

    @admin.action(description="Mark as inactive")
    def make_inactive(self, request, queryset):
        queryset.update(active=0)
        messages.success(
            request, "Selected Party(ies) Marked as Inactive Successfully !!"
        )


class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "writer", "created")


admin.site.register(Gamer, GamerAdmin)
admin.site.register(Videogame, VideogameAdmin)
admin.site.register(Party, PartyAdmin)
admin.site.register(Message, MessageAdmin)
