from django.db import models
from django.contrib.auth.models import User


class ProjectTeam(models.Model):
    STATUS_CHOICES = [
        ("open", "Open"),
        ("closed", "Closed"),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_teams")
    title = models.CharField(max_length=150)
    description = models.TextField()
    subject = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="open")
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, through="TeamMember", related_name="project_teams")

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    ]

    team = models.ForeignKey(ProjectTeam, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"{self.user.username} - {self.team.title}"