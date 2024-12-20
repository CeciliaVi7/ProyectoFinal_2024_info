from django.db import models
from django.contrib.auth.models import AbstractUser, User # Mantener la importación de User si lo usas


# Create your models here.
# Usuarios con atributos nuevos
class User(AbstractUser):
    icono = models.ImageField(upload_to="media/usuarios", null=True, blank=True)
    descripcion = models.TextField(max_length=350, blank=True)  # Hacerlo opcional si es necesario
    date_joined = models.DateTimeField(auto_now_add=True)
    vistas = models.IntegerField(default=0)
    print(User.date_joined)

    def __str__(self):
        return self.username

class Meta: 
     verbose_name="Usuario"
     verbose_name_plural = "Usuarios"



class Categorias(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "Categorias"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Posts(models.Model):  # nombreapp_nombreclase
    titulo = models.CharField(max_length=250, null=False, blank=False, verbose_name="Titulo")
    contenido = models.TextField(verbose_name="Contenido")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="media/posts", null=True, blank=True)
    
    class Meta:
        db_table = "Posts"
        verbose_name = "Posteo"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.titulo



#class Imagenes(models.Model):
    # imagen=models.ImageField(upload_to="/media/posts")
    # post=models.ForeignKey(Posts,on_delete=models.CASCADE)






class Comentarios(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True, null=True)  