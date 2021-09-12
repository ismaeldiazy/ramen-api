from votation.models import (
    RamenYa,
    Vote,
    RamenScore
    )
from rest_framework import serializers

class RamenYaSerializer(serializers.ModelSerializer):
    class Meta:
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
    class Meta:
        model = Vote
        fields = [
            'id',
            'punctuation',
            'ramen',
            'created_at'
            'updated_at'
        ]


class RamenScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = RamenScore
        fields = [
            'id'
            'ramen',
            'total_score',
            'created_at',
            'updated_at'
        ]