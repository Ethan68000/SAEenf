from .forms import DetailsForm
from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect
from datetime import datetime

def index(request):
    liste = list(models.Details.objects.all())
    return render(request, 'Details/index.html',{'liste': liste})


def ajout(request):
    if request.method == "POST":
        form = DetailsForm(request)
        if form.is_valid():
            Details = form.save()
            return render(request, "Details/affiche.html", {"Details": Details})
        else:
            return render(request, "Details/ajout.html", {"form": form})
    else:
        form = DetailsForm()
        return render(request, "Details/ajout.html", {"form": form})

def traitement(request):
    lform = DetailsForm(request.POST)
    if lform.is_valid():
        Details = lform.save()
        return render(request, "Details/affiche.html", {"Details": Details})
    else:
        return render(request, "Details/ajout.html", {"form": lform})

def affiche(request, id):
    Details = models.Details.objects.get(pk=id)
    return render(request, "Donnees/affiche.html", {"Details": Details})

def delete(request, id):
    suppr = models.Details.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/capteur/indexdet",)
