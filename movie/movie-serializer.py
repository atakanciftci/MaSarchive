from rest_framework import serializers
from .models import Movie

class movieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie

        fields = ["movie_name", "category", "poster", "movie_rate", "imdb_page", "duration"]
