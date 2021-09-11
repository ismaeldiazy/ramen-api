from votation.models import (
    RamenYa,
    Vote,
    RamenScore
    )
from rest_framework import serializers

class RamenYaSerializer(serializers.ModelSerializer):
    model = RamenYa
    fields = [
        'id',
        'address',
        'phone_number',
        'website_url',
        'image',
        'created_at',
        'updated_at'
        ]

class VoteSerializer(serializers.ModelSerializer):
    model = Vote
    fields = [
        'id',
        'punctuation',
        'ramen',
        'created_at'
        'updated_at'
    ]

class RamenScoreSerializer(serializers.ModelSerializer):
    model = RamenScore
    fields = [
        'id'
        'ramen',
        'total_score',
        'created_at',
        'updated_at'
    ]