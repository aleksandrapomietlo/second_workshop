from django.db import models


class ConferenceRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.PositiveIntegerField()
    projector_availability = models.BooleanField(default=False)
    objects = models.Manager()


class RoomReservation(models.Model):
    room = models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE)
    date = models.DateField()
    comment = models.TextField(null=True)
    objects = models.Manager()

    class Meta:
        unique_together = ('room_id', 'date',)