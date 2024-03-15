from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render
from .models import Recital, Reserva

# Create your views here.
def index(request):
    recitales = Recital.objects.all()
    context = {'recitales': recitales}
    return render(request, "recitales/index.html", context)

def reservas(request):
    reservas = Reserva.objects.all()
    context = {'reservas': reservas}
    return render(request, "recitales/reservas.html",context)

