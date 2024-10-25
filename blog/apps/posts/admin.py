from django.contrib import admin
from .models import Posts, Categorias, User

# Admin para Posts
class PostsAdmin(admin.ModelAdmin):
    search_fields = ("titulo",)
    list_filter = ["categoria", "autor__username"]
    list_display = ["titulo", "autor", "categoria", "fecha_publicacion"]
    date_hierarchy = "fecha_publicacion"
    ordering = ['-fecha_publicacion']  # Ordenar por fecha de publicación (más reciente primero)

# Admin para User
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')

# Registra los modelos en el admin
admin.site.register(Posts, PostsAdmin)
admin.site.register(Categorias)
admin.site.register(User, UserAdmin)  # Registra el UserAdmin para el modelo User
