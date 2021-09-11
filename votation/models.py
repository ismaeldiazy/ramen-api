from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField
from django.core.validators import RegexValidator

HALF = '0.5'
ONE = '1'
ONE_H = '1.5'
TWO = '2'
TWO_H = '2.5'
THREE = '3'
THREE_H = '3.5'
FOUR = '4'
FOUR_H = '4.5' 
FIVE = '5'
PUNCTUATION_CHOICES = [
    (HALF, 0.5),
    (ONE, 1),
    (ONE_H, 1.5),
    (TWO, 2),
    (TWO_H, 2.5),
    (THREE, 3),
    (THREE_H, 3.5),
    (FOUR, 4),
    (FOUR_H, 4.5),
    (FIVE, 5)
]


class RamenYa(models.Model):
    name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list 
    website_url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

class Vote(models.Model):
    ip = models.GenericIPAddressField(db_index=True, unique=True)
    punctuation = models.DecimalField(choices=PUNCTUATION_CHOICES, max_digits=2, decimal_places=1)
    ramen = models.ForeignKey(RamenYa, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

class RamenScore(models.Model):
    ramen = models.OneToOneField(RamenYa, on_delete=models.CASCADE)
    total_score = models.DecimalField(max_digits=2, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-total_score']
