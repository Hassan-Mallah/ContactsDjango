from django.db import models

# Create your models here.


class Contact(models.Model):
    source_id = models.IntegerField()
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    timestamp = models.DateField()

    def __str__(self):
        return str(self.source_id) + ": " + self.name
