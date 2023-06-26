from .forms import CapteurForm
from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect
import paho.mqtt.client as mqtt

def indexmqtt(request):
    liste = models.Capteur.objects.all()
    return render(request, 'capteur/indexmqtt.html', {"liste": liste})

def ajout(request):
    if request.method == "POST":
        form = CapteurForm(request)
        if form.is_valid():
            Capteur = form.save()
            return render(request, "capteur/affiche.html", {"Capteur": Capteur})
        else:
            return render(request, "capteur/ajout.html", {"form": form})
    else:
        form = CapteurForm()
        return render(request, "capteur/ajout.html", {"form": form})

def traitement(request):
    lform = CapteurForm(request.POST)
    if lform.is_valid():
        Capteur = lform.save()
        return render(request, "capteur/affiche.html", {"Capteur": Capteur})
    else:
        return render(request, "capteur/ajout.html", {"form": lform})


def affiche(request, id):
    Capteur = models.Capteur.objects.get(pk=id)
    return render(request, "capteur/affiche.html", {"Capteur": Capteur})

def index(request):
    liste = models.Capteur.objects.all()
    return render(request, 'capteur/index.html', {"liste": liste})


def delete(request, id):
    suppr = models.Capteur.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/capteur/index",)



def update(request, id):
    Capteur = models.Capteur.objects.get(pk=id)
    aform = CapteurForm(Capteur.dic())
    return render(request, "capteur/ajoutupdate.html/", {"form":aform, "id":id})


def updatetraitement(request, id):
    aform = CapteurForm(request.POST)
    saveid = id
    if aform.is_valid():
        Capteur = aform.save(commit = False)
        Capteur.id = saveid
        Capteur.save()
        return HttpResponseRedirect("/capteur/index/")
    else:
        return render(request, "capteur/ajoutupdate.html", {"form": aform})