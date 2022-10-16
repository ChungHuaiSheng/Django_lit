from django.contrib import admin

from .models import Tracer, Path

# Register your models here.
admin.site.register(Tracer)
admin.site.register(Path)