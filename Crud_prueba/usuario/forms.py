from django.forms import ModelForm
from .models import Usuario, Ciudad, Provincia, Pais


class UsuarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    class Meta:
        model = Usuario
        fields = "__all__"



class crearusuarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(crearusuarioForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Usuario
        fields = "__all__"


class CiudadForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CiudadForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    class Meta:
        model = Ciudad
        fields = "__all__"


class ProvinciaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProvinciaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    class Meta:
        model = Provincia
        fields = "__all__"


class PaisForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PaisForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    class Meta:
        model = Pais
        fields = "__all__"

 