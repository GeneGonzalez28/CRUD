from django.db import models


class Pais(models.Model):
    nombre = models.CharField("Nombre del Pais", max_length=100)
    def __str__(self):
        return f'{self.nombre}'

class Provincia(models.Model):
    nombre = models.CharField("Nombre de la Provincia", max_length=200)
    pais = models.ForeignKey(Pais,null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} {self.pais}' 

class Ciudad(models.Model):
    nombre = models.CharField("Nombre de la Ciudad:", max_length=300)
    provincia = models.ForeignKey(Provincia,null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.nombre} {self.provincia}'

class Usuario(models.Model):
    nombre = models.CharField("Nombre  ", max_length=100)
    apellido = models.CharField("Apellido   ", max_length=100)
    cedula = models.CharField("Cedula        ", max_length=10)
    direccion = models.CharField("Dirección ", max_length=400)
    ciudad = models.ForeignKey(Ciudad,null=True, blank=True, on_delete=models.CASCADE)

    def _str_(self):
        return f'{self.nombre} {self.apellido} {self.cedula} {self.direccion}'