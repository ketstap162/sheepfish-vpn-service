from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Site


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ("url", "alias", "user")
    search_fields = ("url", "alias", "user__username")
