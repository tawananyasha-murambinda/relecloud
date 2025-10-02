from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Cruise(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
