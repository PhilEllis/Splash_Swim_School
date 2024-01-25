from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True
    )
    default_street_address1 = models.CharField(
         max_length=80, null=True, blank=True
    )
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True
    )
    default_county = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


class GuardianProfile(models.Model):
    """
    Model to store guardian profiles.
    Includes personal information about guardians of child users.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    contact_name = models.CharField(max_length=255)
    relationship_to_child = models.CharField(max_length=255)
    emergency_contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class ChildProfile(models.Model):
    """
    Model to store child profiles linked to their guardians.
    """
    guardian = models.ForeignKey(
        GuardianProfile,
        on_delete=models.CASCADE,
        related_name='children'
    )
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    confidence_in_water = models.CharField(
        max_length=50,
        choices=[
            ('Confident', 'Confident'),
            ('Moderate', 'Moderate'),
            ('Poor', 'Poor')
        ]
    )
    medical_conditions = models.TextField(blank=True)
    medication = models.TextField(blank=True)

    def __str__(self):
        return self.name
