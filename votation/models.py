from django.db import models
from django.db.models.deletion import CASCADE


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

# Create your models here.
class RamenYa(models.Model):
    name = models.CharField(max_length=100, blank=True, required=True)
    address = models.CharField(max_length=100, blank=True)
    phonenumber = models.PhoneNumberField(blank=True) 
    website_url = models.URLField(max_length=200)
    image = models.ImageField(uploads_to='media/')
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
