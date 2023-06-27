from . import views, detailsviews
from django.urls import path

from .detailsviews import export_to_csv

urlpatterns = [
                path('ajout/', views.ajout),
                path('traitement/', views.traitement),
                path('index/', views.index),
                path("affiche/<str:id>/", views.affiche),
                path('update/<str:id>/', views.update),
                path('updatetraitement/<str:id>/', views.updatetraitement),
                path("delete/<str:id_capteur>/", views.delete),
                path("bienvenue/",views.bienvenue),
                path('filtre/', views.filtre),


                path('ajoutdet/', detailsviews.ajout),
                path('indexdet/', detailsviews.index),
                path('deletedet/<str:id>/',detailsviews.delete),
                path('traitementdet/',detailsviews.traitement),
                #path('csvdet/', detailsviews.generate_csv, name='generate_csv'),
                path('filtre_datedet/', detailsviews.filtre_date),

                path('export/', export_to_csv, name='export_to_csv'),
    ]