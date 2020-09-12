from django.shortcuts import render, redirect
from .forms import UsuarioForm, CiudadForm, ProvinciaForm, PaisForm
from .models import Usuario, Ciudad, Provincia, Pais

# Create your views here.


# def base(request):
#     if request.method == "POST":
#         usuarioForm = UsuarioForm(request.POST)
#         if usuarioForm.is_valid():
#             instancia = usuarioForm.save(commit=False)
#             instancia.save()
#             return redirect("ciudad")
#     else:
#         usuarioForm = UsuarioForm()
#     return render(request, "usuario.html", {"Formulario": usuarioForm})


def usuario_create(request, plantilla="usuario/usuario_form.html"):
    # return render(request, plantilla)
    if request.method == "POST":
        usuarioForm = UsuarioForm(request.POST)
        if usuarioForm.is_valid():
            usuarioForm.save()
            return redirect("ciudad")
    else:
        usuarioForm = UsuarioForm()
    return render(request, plantilla, {"form": usuarioForm})


def usuario_list(request):
    usuario = Usuario.objects.all()
    contexto = {"usuarios": usuario}
    return render(request, "usuario/usuario_list.html", contexto)


def usuario_edit(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    if request.method == "GET":
        form = UsuarioForm(instance=usuario)
    else:
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
        return redirect("listarusuario")
    return render(request, "usuario/usuario_form.html", {"form": form})


def usuario_delete(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    if request.method == "POST":
        usuario.delete()
        return redirect("listarusuario")
    return render(request, "usuario/usuario_delete.html", {"usuario": usuario})


def ciudad(request):
    if request.method == "POST":
        ciudadForm = CiudadForm(request.POST)
        if ciudadForm.is_valid():
            instancia = ciudadForm.save(commit=False)
            instancia.save()
            return redirect("provincia")
    else:
        ciudadForm = CiudadForm()
    return render(request, "ciudad.html", {"Formulario": ciudadForm})


def provincia(request):
    if request.method == "POST":
        provinciaForm = ProvinciaForm(request.POST)
        if provinciaForm.is_valid():
            instancia = provinciaForm.save(commit=False)
            instancia.save()

            return redirect("pais")
    else:
        provinciaForm = ProvinciaForm()
    return render(request, "provincia.html", {"Formulario": provinciaForm})


def pais(request):
    if request.method == "POST":
        paisForm = PaisForm(request.POST)
        if paisForm.is_valid():
            instancia = paisForm.save(commit=False)
            instancia.save()
            return redirect("crearusuario ")
    else:
        paisForm = PaisForm()
    return render(request, "pais.html", {"Formulario": paisForm})
