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
            'punctuation',
            'ramen',
            'created_at'
            'updated_at'
        ]

class VoteCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = [
            'ip',
            'punctuation',
            'ramen'
        ]
    
    def create(self, validated_data):
        return Vote(**validated_data)
    
    def update(self, instance, validated_data):
        instance.ip = instance.get('ip', instance.ip)
        instance.punctuation = instance.get('punctuation', instance.punctuation)
        instance.ramen = instance.get('ramen', instance.ramen)



class RamenScoreSerializer(serializers.ModelSerializer):
    ramen = RamenYaSerializer(read_only=True)

    class Meta:
        model = RamenScore
        fields = [
            'id',
            'ramen',
            'total_score',
            'created_at',
            'updated_at'
        ]

class RamenScoreCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RamenScore

        fields = [
            'ramen',
            'total_score'
        ]

        def create(self, validated_data):
            return RamenScore(**validated_data)

        def update(self, instance, validated_data):
            instance.ramen = validated_data.get('ramen', instance.ramen)
            instance.total_score = validated_data.get('ramen_score', instance.ramen_score)
            instance.save()
            return instance
