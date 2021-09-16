from votation.models import (
    RamenYa,
    Vote
    )
from rest_framework import serializers

class RamenYaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RamenYa
        fields = [
            'id',
            'name',
            'total_votes',
            'address',
            'phone_number',
            'website_url',
            'image',
            'created_at',
            'updated_at'
            ]

class RamenYaCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RamenYa
        fields = [
            'name',
            'address',
            'phone_number',
            'website_url',
            'image',
            ]
    
    def create(self, validated_data):
        return RamenYa.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
        

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
        instance.ip = validated_data.get('ip', instance.ip)
        instance.ramen = validated_data.get('ramen', instance.ramen)
        instance.save()
        return instance
