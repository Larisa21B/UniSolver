from django.contrib import admin
from .models import AcademicProfile, Skill, AvailabilitySlot

admin.site.register(AcademicProfile)
admin.site.register(Skill)
admin.site.register(AvailabilitySlot)