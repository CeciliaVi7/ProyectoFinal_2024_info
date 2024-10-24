from django.shortcuts import render
from .models import Posts, User
# Create your views here.

#vista basada en funciones
def posts(request):
    ctx = {}  #contextos
    noticias= Posts.objects.all()  # select * from Posts
    ctx["noticias"] = noticias
    print(noticias)
    return render(request, "posts/posts.html", ctx)

def post_id(request, id):
    ctx={}
    noticia= Posts.objects.get(id=id)
    ctx["noticia"]=noticia
    return render(request, "posts/detalle.html", ctx)


def about_us(request):
    return render(request, "posts/about_us.html")

def perfil(request, id):
    
    usuarios = User.objects.get(id=id)
    
    
    ctx = {
        "usuarios": usuarios,
    }
    
    return render(request, "usuarios/perfil.html", ctx)


def lista_usuarios(request):
    usuarios = User.objects.all()  # Se Obtiene todos los usuarios
    ctx = {
        "usuarios": usuarios
    }
    return render(request, "usuarios/lista_usuarios.html", ctx)

#def registro(request):
    #return render (request,"usuarios/registro.html")

#vista basada en clase
from.form import RegistroForm,  CrearForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class Registro(CreateView):
    form_class = RegistroForm  # O el formulario que prefieras
    success_url = reverse_lazy("noticias")
    template_name = "usuarios/registro.html"

class CrearPost(CreateView):
    form_class = CrearForm
    model = Posts
    template_name = "posts/crear_post.html"
    success_url = reverse_lazy("noticias")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
class BorrarPost(DeleteView):
    model = Posts
    template_name = 'posts/posts_confirm_delete.html'
    success_url = reverse_lazy("noticias")


    