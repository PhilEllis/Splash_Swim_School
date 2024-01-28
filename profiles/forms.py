from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms.widgets import DateInput
from .models import UserProfile, GuardianProfile, ChildProfile


class UserProfileForm(forms.ModelForm):
    """
    Form for creating and updating a user profile.
    """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        # Define regex validator for UK phone number
        phone_regex = RegexValidator(
            regex=r'^0\d{10}$',
            message=("UK Phone number must start with '0' and be exactly "
                     "11 digits long.")
        )
        self.fields['default_phone_number'].validators.append(
            phone_regex
        )  # Apply the regex validator to the phone number field
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'mb-2 profile-form-input'
            )
            self.fields[field].label = False


class GuardianProfileForm(forms.ModelForm):
    """
    Form for creating and updating a guardian profile.
    Vital emergency contact information.
    """
    class Meta:
        model = GuardianProfile
        fields = [
            'contact_name', 'relationship_to_child',
            'emergency_contact_number'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'contact_name': 'Contact Name',
            'relationship_to_child': 'Relationship to Child',
            'emergency_contact_number': 'Emergency Contact Number',
        }

        # Define regex validator for UK phone number
        phone_regex = RegexValidator(
            regex=r'^0\d{10}$',
            message=("UK Phone number must start with '0' and be exactly "
                     "11 digits long.")
        )
        self.fields['emergency_contact_number'].validators.append(phone_regex)

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'mb-2 profile-form-input'
            )
            self.fields[field].label = False


class ChildProfileForm(forms.ModelForm):
    """
    Form for creating and updating a child's profile.
    Includes personal info and swimming ability.
    """
    class Meta:
        model = ChildProfile
        fields = [
            'name', 'date_of_birth', 'confidence_in_water',
            'medical_conditions', 'medication'
        ]
        widgets = {
            'date_of_birth': DateInput(attrs={
                'class': 'mb-2 profile-form-input',
                'type': 'date'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Child’s Name',
            'medical_conditions': 'Medical Conditions',
            'medication': 'Medication',
        }

        # Set the label for 'date_of_birth'
        self.fields['date_of_birth'].label = 'Date of Birth (YYYY-MM-DD)'

        for field in self.fields:
            if field in placeholders:
                self.fields[field].widget.attrs['placeholder'] = (
                    placeholders[field]
                )
            if field != 'confidence_in_water' and field != 'date_of_birth':
                self.fields[field].label = False
