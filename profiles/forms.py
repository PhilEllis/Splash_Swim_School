from django import forms
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Child’s Name',
            'date_of_birth': 'Date of Birth (YYYY-MM-DD)',
            'confidence_in_water': 'Confidence in Water',
            'medical_conditions': 'Medical Conditions',
            'medication': 'Medication',
        }

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
            if field == 'date_of_birth':
                self.fields[field].widget.attrs['type'] = 'date'
