from rest_framework import viewsets
from .models import ProjectTeam, TeamMember
from .serializers import ProjectTeamSerializer, TeamMemberSerializer


class ProjectTeamViewSet(viewsets.ModelViewSet):
    queryset = ProjectTeam.objects.all()
    serializer_class = ProjectTeamSerializer


class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer