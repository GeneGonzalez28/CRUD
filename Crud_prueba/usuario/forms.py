from django.forms import ModelForm
from .models import Usuario, Ciudad, Provincia, Pais


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"



class crearusuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"


class CiudadForm(ModelForm):
    class Meta:
        model = Ciudad
        fields = "__all__"


class ProvinciaForm(ModelForm):
    class Meta:
        model = Provincia
        fields = "__all__"


class PaisForm(ModelForm):
    class Meta:
        model = Pais
        fields = "__all__"
