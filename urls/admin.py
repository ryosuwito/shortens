from django.contrib import admin
from .models import Shortens

class ShortensAdmin(admin.ModelAdmin):
    model = Shortens

admin.site.register(Shortens, ShortensAdmin)
