from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms

class CapteurForm(ModelForm):
    class Meta:
        model = models.Capteur
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_capteur'].widget.attrs['class'] = 'form-select'
        self.fields['id_capteur'].widget.choices = [(capteur.id_capteur, capteur.id_capteur) for capteur in models.Capteur.objects.all()]

class DetailsForm(ModelForm):
    class Meta:
        model = models.Details
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['class'] = 'form-select'
        self.fields['date'].widget.choices = [(capteur.id_capteur, capteur.id_capteur) for capteur in models.Details.objects.all()]

class CapteurFormupdate(ModelForm):
    class Meta:
        model = models.Capteur
        fields = "__all__"
