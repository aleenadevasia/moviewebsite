from rest_framework import serializers
from .models import Movie
from .models import Review
from categories.models import Category


class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'poster', 'description', 'release_date', 'director', 'writer', 'musician', 'cast', 'category', 'trailer_link']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request and request.user.is_authenticated else None
        if user:
            validated_data['added_by'] = user
        else:
            raise serializers.ValidationError("User authentication required.")
        return super().create(validated_data)

class MovieDetailSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'movie', 'user', 'rating', 'comment']
