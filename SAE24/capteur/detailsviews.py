import csv
from .forms import DetailsForm
from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime, date
from matplotlib import pyplot as plt


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


def filtre_date(request):
    if request.method == 'POST':
        date_debut = request.POST.get('date_debut')
        date_fin = request.POST.get('date_fin')
        donnees_filtrees = models.Details.objects.filter(date__range=[date_debut, date_fin])
        return render(request, 'Details/filtre_date.html', {'donnees_filtrees': donnees_filtrees})
    else:
        return render(request, 'Details/filtre_date.html')


def graphique(request):
    data = models.Details.objects.all()

    # Conversion des objets datetime.time en chaînes de caractères
    dates = [entry.time.strftime('%H:%M:%S') for entry in data]
    temperatures = [entry.temp for entry in data]

    plt.plot(dates, temperatures)

    plt.xlabel('heure')
    plt.ylabel('Température (°C)')
    plt.title('Évolution de la température')

    plt.show()

    return HttpResponseRedirect("/capteur/indexdet/")


def refresh(request):
    if request.method == 'POST':
        choix = request.POST.get('choix')
        if choix == 'auto':
            message = "Rafraîchissement automatique"
            rafraichissement = 3  # Nombre de secondes avant chaque rafraîchissement
        elif choix == 'manuel':
            nb_secondes = request.POST.get('nb_secondes')
            try:
                rafraichissement = int(nb_secondes)
                message = "Rafraîchissement manuel"
            except ValueError:
                message = "Veuillez entrer un nombre entier valide."
                rafraichissement = 0
        else:
            message = "Choix invalide."
            rafraichissement = 0
    else:
        message = ""
        rafraichissement = 0

    context = {
        'message': message,
        'rafraichissement': rafraichissement
    }

    return render(request, 'capteur/indexdet.html', context)


def choisir(request):
    if request.method == 'POST':
        choix = request.POST.get('choix')
        if choix == 'auto':
            rafraichissement = 3  # Rafraîchissement automatique toutes les 3 secondes
        elif choix == 'manuel':
            nb_secondes = request.POST.get('nb_secondes')
            try:
                rafraichissement = int(nb_secondes)
            except ValueError:
                rafraichissement = 0
        else:
            rafraichissement = 0

        return redirect('indexdet')
    else:
        return redirect('indexdet')