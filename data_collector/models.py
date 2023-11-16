from django.db import models

class AdData(models.Model):
    source = models.CharField(max_length=100)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.source} data for {self.date}"