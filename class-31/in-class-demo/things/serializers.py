# Serializers change the django models into JSON
from rest_framework import serializers
# The model we are serializing (representing as JSON)
from .models import Thing

# Take `Thing` and make it JSON. Like a translator


class ThingSerializer(serializers.ModelSerializer):
    # Defines an inner class, Meta, which is used to specify metadata about the serializer class.
    class Meta:
        fields = ('id', 'owner', 'name', 'description', 'created_at')  # could also use '__all__'
        model = Thing  # the model to serialize
