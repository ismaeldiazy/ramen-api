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
            'name',
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
            'ip',
            'ramen',
            'created_at',
            'updated_at'
        ]

class VoteCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = [
            'ip',
            'ramen'
        ]
    
    def create(self, validated_data):
        return Vote.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.ip = instance.get('ip', instance.ip)
        instance.ramen = instance.get('ramen', instance.ramen)


class RamenScoreSerializer(serializers.ModelSerializer):
    ramen = RamenYaSerializer(read_only=True)

    class Meta:
        model = RamenScore
        fields = [
            'id',
            'ramen',
            'total_votes',
            'created_at',
            'updated_at'
        ]


class RamenScoreCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RamenScore

        fields = [
            'ramen',
            'total_votes'
        ]

        def create(self, validated_data):
            return RamenScore.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.ramen = validated_data.get('ramen', instance.ramen)
            instance.total_votes = validated_data.get('total_votes', instance.ramen_score)
            instance.save()
            return instance
