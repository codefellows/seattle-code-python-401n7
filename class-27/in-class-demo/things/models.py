from django.db import models
from django.contrib.auth import get_user_model


class Thing(models.Model):
    # Create a class variable for each field
    # Assign a field type, and include field options
    name = models.CharField(max_length=256)
    rating = models.IntegerField(default=0)
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
