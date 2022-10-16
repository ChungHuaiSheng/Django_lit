from django.db import models

# Create your models here.
class Path(models.Model):
    part_id = models.CharField(max_length=6)
    reticle_id = models.CharField(max_length=10)
    eqp_id = models.CharField(max_length=6)
    lot_id = models.CharField(max_length=8)

class Tracer(models.Model):
    trace_path = models.ForeignKey(Path, on_delete=models.CASCADE)