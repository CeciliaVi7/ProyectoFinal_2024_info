from django.shortcuts import render , redirect, get_object_or_404
from .models import Posts, User, Comentarios, Categorias
from.form import RegistroForm,  CrearForm, ModificarForm,ComentarioForm, ModificarComentarioForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from.form import CustomLoginForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

# Create your views here.

#vista basada en funciones
def posts(request):
    ctx = {}  #contextos
    noticias= Posts.objects.all().order_by("-id") # select * from Posts
    ctx["noticias"] = noticias
    print(noticias)
    return render(request, "posts/posts.html", ctx)

from django.views.generic import ListView
from .models import Posts

class Noticias(ListView):
    model = Posts
    template_name = "posts/posts.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        ordenar_por = self.request.GET.get("ordenar")
        print(ordenar_por)

        if ordenar_por == "fecha":
            queryset = queryset.order_by("-fecha_publicacion")
        elif ordenar_por == "alfabetico":
            queryset = queryset.order_by("titulo")  
# Filtrar por autor
        autor = self.request.GET.get("autor")
        if autor:
         queryset = queryset.filter(autor__username=autor)
        return queryset
    # por categorias
        categoria = self.request.GET.get("categoria")
        if categoria:
            queryset = queryset.filter(categoria__nombre=categoria)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"]=Categorias.objects.all()
        return context



def post_id(request, id):
    ctx = {}
    noticia = Posts.objects.get(id=id)
    comentarios = Comentarios.objects.filter(post=noticia)
    ctx["noticia"] = noticia
    ctx["comentarios"] = comentarios
    return render(request, "posts/detalle.html", ctx)


def about_us(request):
    return render(request, "posts/about_us.html")

def perfil(request, id):
    
    usuarios = User.objects.get(id=id)
    ctx = {
        "usuarios": usuarios,
    }
    return render(request, "usuarios/perfil.html", ctx)




#def registro(request):
    #return render (request,"usuarios/registro.html")

#vista basada en clase

class Registro(CreateView):
    form_class = RegistroForm  
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

class ModificarPost(UpdateView):
    model = Posts
    template_name = "posts/modificar_post.html"
    form_class = ModificarForm
    success_url = reverse_lazy("noticias")





def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.get_user()
            login(request, user)

            # duración de la sesión
            if form.cleaned_data.get('remember_me'):
                request.session.set_expiry(1209600)  # 2 semanas
            else:
                request.session.set_expiry(0)  

            return redirect('noticias')  
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})




@login_required
def comentar_post(request, post_id):
    if request.method == 'POST':
        comentario = request.POST.get("comentario", None)
        user = request.user

        
        try:
            get_post = Posts.objects.get(pk=post_id)  
            Comentarios.objects.create(autor=user, contenido=comentario, post=get_post)
            return redirect('detalle', id=post_id)  #
        except Posts.DoesNotExist:
            
            return redirect('noticias')  

    return redirect('noticias')  

class ModificarComentario(UpdateView):
    model=Comentarios
    form_class = ModificarComentarioForm
    template_name="comentarios/modificar.html"
    success_url= reverse_lazy("noticias")

class EliminarComentario(DeleteView):
    model = Comentarios
    template_name = "comentarios/confirm_delete.html"
    success_url = reverse_lazy("noticias")



def perfil_usuario(request, username):
    usuario = get_object_or_404(User, username=username)
    posts = Posts.objects.filter(autor=usuario)  

    return render(request, 'perfil.html', {  
        'usuario': usuario,
        'posts': posts,
    })
