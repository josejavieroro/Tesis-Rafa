from django.db import models

class Facultad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)


class Carrera(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    facultad = models.ForeignKey(Facultad,on_delete=models.CASCADE)


class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ci = models.BigIntegerField()
    facultad = models.ForeignKey(Facultad,on_delete=models.CASCADE)
    departamento = models.CharField(max_length=100)

class Tribunal(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    fecha =  models.DateTimeField()


class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ci = models.BigIntegerField()
    anno = models.IntegerField()
    carrera = models.ForeignKey(Carrera,on_delete=models.DO_NOTHING)


class Tesis(models.Model):
    id = models.AutoField(primary_key=True)
    tema = models.CharField(max_length=500)
    estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)


class TRibunalTesisTutor(models.Model):
    id = models.AutoField(primary_key=True)
    tesis = models.ForeignKey(Tesis,on_delete=models.CASCADE)
    tutor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

class TRibunalTesisOponente(models.Model):
    id = models.AutoField(primary_key=True)
    tesis = models.ForeignKey(Tesis,on_delete=models.CASCADE)
    oponente = models.ForeignKey(Profesor, on_delete=models.CASCADE)


class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    direccion = models.CharField(max_length=500)

class Ubicacion(models.Model):
    id = models.AutoField(primary_key=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)

class Expediente(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    evaluacion = models.CharField(max_length=500)
    promedio = models.DecimalField(max_digits=3,decimal_places=2)
    fechaReunion = models.DateTimeField()
