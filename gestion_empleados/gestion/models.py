from django.db import models

# Create your models here.
class Salarios(models.Model):
    monto = models.IntegerField()
    cobro_año = models.BooleanField(blank=False) 
    pago_extra = models.BooleanField(blank=False)

    
class PuestoTrabajo(models.Model):
    nombre_cargo = models.CharField(max_length=30)
    salario = models.IntegerField()
    salario_monto = models.ForeignKey(Salarios,on_delete= models.CASCADE)


class Pais(models.Model):
    nombre_pais = models.CharField(max_length=100)


class Poblacion(models.Model):
    nombre_poblacion = models.CharField(max_length=200)
    Pais = models.ForeignKey(Pais, on_delete= models.CASCADE)


class Fabricas(models.Model):
    nombre_fabrica = models.CharField(max_length=100)
    direccion2 = models.CharField(max_length=100)
    codigo_postal = models.IntegerField()
    Poblacion = models.ForeignKey(Poblacion, on_delete= models.CASCADE)
    

class Empleados(models.Model):
    documento = models.IntegerField()
    nombre = models.CharField(max_length=20)
    email = models.EmailField()
    direccion = models.CharField(max_length=100)
    puesto_trabajo = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=50)
    name_cargo = models.ForeignKey(PuestoTrabajo, on_delete= models.CASCADE)
    name_fabrica = models.ForeignKey(Fabricas,on_delete= models.CASCADE)
        
   

    