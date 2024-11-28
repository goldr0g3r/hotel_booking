from django.contrib import admin
from useraccounts.models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "name", "is_active", "is_staff", "is_superuser"]
    list_display_links = ["id", "email", "name"]
    list_filter = ["is_active", "is_staff", "is_superuser"]
    search_fields = ["email", "name"]
    list_per_page = 25


admin.site.register(User, UserAdmin)
