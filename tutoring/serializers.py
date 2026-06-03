from rest_framework import serializers
from .models import TutoringRequest


class TutoringRequestSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.username')

    class Meta:
        model = TutoringRequest
        fields = ['id', 'student', 'tutor', 'subject', 'message', 'status', 'created_at']
        read_only_fields = ['student', 'status', 'created_at']