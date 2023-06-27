from . import views, detailsviews
from django.urls import path
from .views import index

urlpatterns = [
                path('ajout/', views.ajout),
                path('traitement/', views.traitement),
                path('index/', views.index, name='index'),
                path("affiche/<str:id>/", views.affiche),
                path('update/<str:id>/', views.update),
                path('updatetraitement/<str:id>/', views.updatetraitement),
                path("delete/<str:id_capteur>/", views.delete),
                path("bienvenue/",views.bienvenue),
                path('filtre/', views.filtre),
                path('refresh/',views.refresh, name='refresh'),
                path('choisir/', views.choisir, name='choisir'),


                path('ajoutdet/', detailsviews.ajout),
                path('indexdet/', detailsviews.index, name='indexdet'),
                path('deletedet/<str:id>/',detailsviews.delete),
                path('traitementdet/',detailsviews.traitement),
                path('csv/', views.generate_csv,),
                path('filtre_datedet/', detailsviews.filtre_date),
                path('refreshdet/',views.refresh, name='refreshdet'),
                path('choisirdet/', detailsviews.choisir, name='choisirdet'),

    ]