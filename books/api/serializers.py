from rest_framework import serializers
from books import models

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        fields = ('id_book', 'title', 'author', 'release_year', 'state', 'image')
        # fields = '__all__'
        # extra_kwargs = {'user': {'read_only': True}}

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = ('id', 'email', 'username', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.Users.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )

        return user