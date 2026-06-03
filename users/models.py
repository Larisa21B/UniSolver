from django.db import models
from django.contrib.auth.models import User


class AcademicProfile(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student/Elev'),
        ('tutor', 'Tutor'),
        ('admin', 'Admin'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="academic_profile"
    )

    university = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    study_year = models.IntegerField()
    bio = models.TextField(blank=True)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='student'
    )

    def __str__(self):
        return f"{self.user.username} - {self.specialization}"


class Skill(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="skills"
    )

    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.subject}"


class SkillAvailability(models.Model):
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name="availabilities"
    )

    available_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.skill.subject} - {self.available_date} {self.start_time}-{self.end_time}"


class AvailabilitySlot(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="availability_slots"
    )

    day_of_week = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.user.username} - {self.day_of_week} {self.start_time}-{self.end_time}"