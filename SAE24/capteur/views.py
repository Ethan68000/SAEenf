from .forms import CapteurForm, CapteurFormupdate
from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect


def bienvenue(request):
    liste = models.Capteur.objects.all()
    return render(request, 'capteur/bienvenue.html', {"liste": liste})

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
    form = CapteurFormupdate(Capteur.dic())
    temp = models.Capteur.objects.get(pk=id)
    temp.save()
    return render(request, "capteur/update.html", {"form":form, "id":id})

def updatetraitement(request, id):
    form = CapteurFormupdate(request.POST)
    saveid = id
    piece = models.Capteur.objects.get(pk=id).piece
    if form.is_valid():
        Capteur = form.save(commit = False)
        Capteur.id = saveid
        Capteur.piece = piece
        Capteur.save()
        return HttpResponseRedirect("/capteur/index")
    else:
        return HttpResponseRedirect(f"/capteur/update/{saveid}/")