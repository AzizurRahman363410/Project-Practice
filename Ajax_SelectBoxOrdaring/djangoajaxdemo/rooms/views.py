from django.shortcuts import render,get_object_or_404
# from django.views.generic import View
from django.http import JsonResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from .models import Room
from django.views.generic.edit import CreateView,View
from django.views import View
class  RoomForm(forms.ModelForm):
    class  Meta:
        model = Room
        fields =  '__all__'

class  RoomList(View):

    def  get(self, request):
        rooms = []
        rooms =  list(Room.objects.all().values())
        value = self.request.GET.get('value',)
        print('data  value is : ',value)
        if value == 'name':
            rooms =  list(Room.objects.all().values().order_by('name'))
        elif value == 'new':
            rooms =  list(Room.objects.all().values().order_by('-id'))
        elif value == 'room':
            rooms =  list(Room.objects.all().values().order_by('room_number'))
        else:
            rooms =  list(Room.objects.all().values().order_by('name'))
        # print('room is :',rooms)
        print('room is : ',rooms)
        data =  dict()
        data['rooms'] = rooms
        return JsonResponse(data)

class  RoomDetail(View):
    def  get(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        data =  dict()
        data['room'] = model_to_dict(room)
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class  RoomCreate(CreateView):
    def  post(self, request):
        data =  dict()
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            data['room'] = model_to_dict(room)
        else:
            data['error'] =  "form not valid!"
        return JsonResponse(data)

class  RoomUpdate(View):
    def  post(self, request, pk):
        data =  dict()
        room = Room.objects.get(pk=pk)
        form = RoomForm(instance=room, data=request.POST)
        if form.is_valid():
            room = form.save()
            data['room'] = model_to_dict(room)
        else:
            data['error'] =  "form not valid!"
        return JsonResponse(data)


# for method function csrf_token
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt



from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt, name='dispatch')
class  RoomDelete(View):
    def  post(self, request, pk):
        data =  dict()
        room = Room.objects.get(pk=pk)
        if room:
            room.delete()
            data['message'] =  "Room deleted!"
        else:
            data['message'] =  "Error!"
        return JsonResponse(data)