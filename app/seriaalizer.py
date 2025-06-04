from rest_framework import serializers

from app.models import Person

#convert from/to json
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


#ngrok http --url =amused-internally-cow.ngrok-free.app 8000

# https://amused-internally-cow.ngrok-free.app