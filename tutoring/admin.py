from django.contrib import admin
from .models import TutoringRequest, TutoringSession

admin.site.register(TutoringRequest)
admin.site.register(TutoringSession)