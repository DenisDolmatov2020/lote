import os
from datetime import date, timedelta
from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from tracker.models import Tracker
from tracker.serializers import TrackerSerializer


class TrackerView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def add_energy(self, energy):
        self.request.user.energy += energy \
            if energy < int(os.environ.get("MAX_BONUS")) else int(os.environ.get("MAX_BONUS")) - 1
        self.request.user.save(update_fields=['energy'])

    def get(self, request):
        tracker, create = Tracker.objects.get_or_create(user=self.request.user)
        yesterday = date.today() - timedelta(days=1)
        if not create and tracker.date <= yesterday:
            tracker.days_row = 1 if tracker.date < yesterday else tracker.days_row + 1
            create = True
        if create:
            self.add_energy(tracker.days_row)
        tracker.save()
        serializer = TrackerSerializer(data=tracker.__dict__)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED if create else status.HTTP_200_OK)
