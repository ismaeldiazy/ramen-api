from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField
from django.core.validators import RegexValidator

ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
PUNCTUATION_CHOICES = [
    (ONE, "one"),
    (TWO, "two"),
    (THREE, "three"),
    (FOUR, "four"),
    (FIVE, "five"),
]


class RamenYa(models.Model):
    name = models.CharField(max_length=100, blank=True)
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
    punctuation = models.PositiveSmallIntegerField(choices=PUNCTUATION_CHOICES)
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
