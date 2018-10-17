from django.db import models

class Shortens(models.Model):
    hash = models.CharField(db_index=True,
            max_length = 100)
    origin = models.CharField(max_length=1000,
            db_index=True)
