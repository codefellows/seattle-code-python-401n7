# Serializers change the django models into JSON
from rest_framework import serializers
from .models import Thing

# Take `Thing` and make it JSON. Like a translator

class ThingSerializer(serializers.ModelSerializer)
