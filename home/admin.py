from django.contrib import admin
from home.models import Scdg
class ScdgAdmin(admin.ModelAdmin):
    list_display=('title','url')
admin.site.register(Scdg, ScdgAdmin)