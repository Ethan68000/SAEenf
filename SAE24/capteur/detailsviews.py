import csv
from .forms import DetailsForm
from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime, date


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


import csv
from django.http import HttpResponse
from django.template import loader

def export_to_csv(request):
    liste = ['valeur1', 'valeur2', 'valeur3']  # Exemple de liste de données

    template = loader.get_template('export_template.txt')
    context = {'liste': liste}
    rendered_template = template.render(context)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="donnees.csv"'

    csv_writer = csv.writer(response)

    for line in rendered_template.splitlines():
        csv_writer.writerow([line])

    return response



def filtre_date(request):
    details = models.Details.objects.all()

    if request.method == 'POST':
        date = request.POST.get('date')

        if not date:
            return render(request, 'capteur/filtre_datedet.html', {'erreur'})

        try:
            details = models.Details.objects.filter(date=date)
        except models.Details.DoesNotExist:
            return render(request, 'capteur/filtre_datedet.html', {'erreur': 'Aucune donnée disponible pour la date spécifiée.'})

        context = {
            'donnees': details,
            'date': date,
        }

        return render(request, 'capteur/filtre_datedet.html', context)

    context = {
        'donnees': details,
    }

    return HttpResponseRedirect("/capteur/filtre_datedet",)


