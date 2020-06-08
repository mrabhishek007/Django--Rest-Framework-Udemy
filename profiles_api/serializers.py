from rest_framework import serializers

from profiles_api.models import UserProfile


class HelloSerializer(serializers.Serializer):
    """ Serializers a name field for testing our APIView """
    name = serializers.CharField(max_length=10)


# Creating  a profile Serialzer which will manage user profiles overridden in usermodel.py
class UserSerializers(serializers.ModelSerializer):
    """ Serializers a User profile Object """

    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'email', 'password')

        # Hashing the password by mentioning the password field
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    # Overriding the default behaviour of saving object in db
    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user
