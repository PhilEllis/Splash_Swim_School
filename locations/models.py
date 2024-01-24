from django.db import models


# Create your models here.
class Location(models.Model):
    """
    Model representing a location and it's max capacity.
    """

    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        """
        Return the location name as its string representation.
        """
        return self.name
