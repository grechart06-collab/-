from django.shortcuts import render
from .models import Мероприятие

def index(request):
    events = Мероприятие.objects.all()
    return render(request, 'main/index.html',{'events': events})
