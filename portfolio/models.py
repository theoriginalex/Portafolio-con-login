from django.db import models
from datetime import date
import datetime

# Create your models here.
#PORTAFOLIOS
class Project(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to="static/portfolio/images")
    url = models.URLField(blank=True)
    fecha = models.DateField(default=date.today)

    def __str__(self) -> str:
        return f"{self.titulo}, {self.descripcion}, {self.imagen}, {self.url}, {self.fecha}"

#BLOGS
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="static/blog/images")
    fecha = models.DateField(default=datetime.date.today)

    def __str__(self) -> str:
        return f"{self.titulo}, {self.descripcion}, {self.imagen}, {self.fecha}"


#EXPERIENCIA
class Curso(models.Model):
    institucion_del_curso = models.CharField(max_length=255)
    descripcion_curso = models.TextField()
    fecha_curso = models.DateField()
    numero_horas = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.institucion_del_curso}: {self.descripcion_curso} ({self.fecha_curso}, {self.numero_horas} horas)"
        