from django.contrib import admin
from .models import ChildProfile, GuardianProfile


class ChildProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'guardian_info', 'confidence_in_water', 'medical_conditions', 'medication')

    def guardian_info(self, obj):
        guardian = obj.guardian
        return f"{guardian.contact_name} ({guardian.relationship_to_child}), Emergency Contact: {guardian.emergency_contact_number}"
    guardian_info.short_description = 'Guardian Details'

# Register your models here.
admin.site.register(ChildProfile, ChildProfileAdmin)