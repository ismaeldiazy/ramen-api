from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField
from django.core.validators import RegexValidator


class RamenYa(models.Model):
    name = models.CharField(max_length=100, blank=True)
    total_votes = models.PositiveBigIntegerField(blank=True, default=0)
    address = models.CharField(max_length=100, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list 
    website_url = models.URLField(max_length=200)
    image = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']


class Vote(models.Model):
    ip = models.GenericIPAddressField(db_index=True, unique=True)
    ramen = models.ForeignKey(RamenYa, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
