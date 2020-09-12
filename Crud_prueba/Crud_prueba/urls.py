"""Crud_prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuario.views import ciudad, provincia, pais, usuario_create, usuario_list, usuario_edit, usuario_delete



urlpatterns = [
    #path("admin/", admin.site.urls),
    #path("", base, name="usuario"),
    path("ciudad/", ciudad, name="ciudad"),
    path("provincia/", provincia, name="provincia"),
    path("pais/", pais, name="pais"),

    path("usuario/crear", usuario_create, name="crearusuario"),
    path("usuario/listar", usuario_list, name="listarusuario"),
    path("usuario/eliminar/<int:id_usuario>/", usuario_delete, name="eliminarusuario"),
    path("usuario/editar/<int:id_usuario>/", usuario_edit, name="editarusuario"),
]