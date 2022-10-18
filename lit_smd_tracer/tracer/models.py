from django.db import models
from django.contrib import admin


# Create your models here.
class Path(models.Model):
    part_id = models.CharField(max_length=6)
    reticle_id = models.CharField(max_length=10)
    eqp_id = models.CharField(max_length=6)
    lot_id = models.CharField(max_length=8)
    wafer_id = models.CharField(max_length=8)
    create_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.wafer_id


class Tracer(models.Model):
    trace_path = models.ForeignKey(Path, on_delete=models.CASCADE)

    def __str__(self):
        return self.trace_path


class PathAdmin(admin.ModelAdmin):
    list_display = ('id', 'wafer_id')
