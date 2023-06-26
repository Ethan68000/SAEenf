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

def affiche(request, id):
    Details = models.Details.objects.get(pk=id)
    return render(request, "Donnees/affiche.html", {"Details": Details})