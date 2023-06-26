from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class CapteurForm(ModelForm):
    class Meta:
        model = models.Capteur
        fields = "__all__"


class DetailsForm(ModelForm):
    class Meta:
        model = models.Details
        fields = "__all__"