#urls solo de la aplicacion posts
from django.urls import path
from. import views

urlpatterns = [
  
    # vbc
  path("", views.Noticias.as_view(), name="noticias"),
  path("about/", views.about_us, name="about") ,
  path("registro/", views.Registro.as_view(), name="registro"),

  path("detalle/<int:id>/", views.post_id, name="detalle"),
  # perfil del usuario
  path("perfil/<int:id>/", views.perfil, name="perfil"),
  # crear nuevo post
  path("nuevo_post/", views.CrearPost.as_view(), name="nuevo_post"),
  #Eliminar post
  path("borrar/<int:pk>/", views.BorrarPost.as_view(), name="borrar_post"),
  #modificar post
  path("modificar/<int:pk>/", views.ModificarPost.as_view(), name="modificar_post"),
  #Comentario
  path("comentar/<int:post_id>/", views.comentar_post, name="comentar"),
  #Modificar Comentario
  path("modificar_com/<int:pk>",views.ModificarComentario.as_view(),name="modificar_comentario",),
  #Eliminar Comentario
  path("borrar/<int:pk>", views.EliminarComentario.as_view(), name="borrar_comentario"),
  

  
]