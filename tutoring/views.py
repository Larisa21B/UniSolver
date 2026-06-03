from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import TutoringRequest
from .serializers import TutoringRequestSerializer


class TutoringRequestViewSet(viewsets.ModelViewSet):
    serializer_class = TutoringRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return TutoringRequest.objects.filter(student=user) | TutoringRequest.objects.filter(tutor=user)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)