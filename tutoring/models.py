from django.db import models
from django.contrib.auth.models import User


class TutoringRequest(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_tutoring_requests"
    )

    tutor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="received_tutoring_requests"
    )

    subject = models.CharField(max_length=100)
    message = models.TextField()

    requested_date = models.DateField(null=True, blank=True)
    requested_start_time = models.TimeField(null=True, blank=True)
    requested_end_time = models.TimeField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} -> {self.tutor.username} ({self.subject})"


class TutoringSession(models.Model):
    STATUS_CHOICES = [
        ("scheduled", "Scheduled"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="student_sessions"
    )

    tutor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tutor_sessions"
    )

    subject = models.CharField(max_length=100)
    session_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="scheduled"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} cu {self.tutor.username} - {self.subject}"