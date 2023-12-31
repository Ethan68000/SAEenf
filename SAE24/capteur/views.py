import csv

from .forms import CapteurForm, CapteurFormupdate
from django.shortcuts import render, redirect
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


def delete(request, id_capteur):
    if request.method == 'POST':
        Capteur = models.Capteur.objects.get(pk=id_capteur)
        # Supprimer les enregistrements liés dans la table "details"
        Capteur.details_set.all().delete()
        Capteur.delete()
        return redirect('index')
    else:
        Capteur = models.Capteur.objects.get(pk=id_capteur)
        return render(request, "capteur/delete.html", {"Capteur": Capteur})



def update(request, id):
    Capteur = models.Capteur.objects.get(pk=id)
    aform = CapteurForm(Capteur.dic())
    return render(request, "capteur/ajoutupdate.html/", {"form":aform, "id":id})

def filtre(request):
    capteurs = models.Capteur.objects.all()

    if request.method == 'POST':
        id_capteur = request.POST.get('id_capteur')

        if not id_capteur:
            return render(request, 'capteur/filtre.html', {'erreur'})

        try:
            capteur = models.Capteur.objects.get(id_capteur=id_capteur)
        except models.Capteur.DoesNotExist:
            return render(request, 'capteur/filtre.html', {'erreur': 'Le capteur spécifié n\'existe pas.'})

        donnees = models.Details.objects.filter(id_capteur=capteur)

        context = {
            'donnees': donnees,
            'capteur': capteur,
            'capteurs': capteurs
        }

        return render(request, 'capteur/filtre.html', context)

    context = {
        'capteurs': capteurs
    }

    return render(request, 'capteur/filtre.html', context)
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

from django.http import HttpResponse
def generate_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Colonne1', 'Colonne2', 'Colonne3', 'Colonne4'])

    data = models.Details.objects.all()
    for item in data:
        writer.writerow([item.id_capteur, item.date, item.time,item.temp])

    return response


from django.shortcuts import render, redirect

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

    return render(request, 'capteur/index.html', context)


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

        return redirect('index')
    else:
        return redirect('index')
