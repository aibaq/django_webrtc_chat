from django.views import View
from django.shortcuts import render
from .models import *


class RoomView(View):
    template_name = 'core/index.html'

    def get(self, request, name):
        room, _ = Room.objects.get_or_create(name=name)
        return render(request, self.template_name, {'room': room})
