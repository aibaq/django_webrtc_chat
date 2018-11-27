from channels.db import database_sync_to_async
from django.db import models


class TimestampMixin(models.Model):
    class Meta:
        abstract = True
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения')


class RoomManager(models.Manager):

    @database_sync_to_async
    def get_async(self, name):
        room, _ = Room.objects.get_or_create(name=name)
        return room


class Room(TimestampMixin, models.Model):
    name = models.CharField(max_length=1000, primary_key=True)
    objects = RoomManager()
