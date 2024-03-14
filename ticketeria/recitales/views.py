from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render
from .models import Recital

# Create your views here.
def index(request):
    recitales = Recital.objects.all()
    context = {'recitales': recitales}
    return render(request, "recitales/index.html", context)

def reservas(request):
    context = {}
    return render(request, "recitales/reservas.html",context)

"""
def vuelo(request, id_vuelo):
    try:
        vuelo = Recital.objects.get(id=id_vuelo)
        return render(request, "vuelos/vuelo.html", {
            "vuelo": vuelo,
            "pasajeros": vuelo.pasajeros.all()
        })
    except Vuelo.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))"""