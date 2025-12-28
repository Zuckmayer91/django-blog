from django.contrib import admin
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Campos que se verán en la lista del administrador
    list_display = ['title', 'user', 'created_at']
    
    # Esto hace que el slug se complete solo (ahorra mucho tiempo)
    prepopulated_fields = {'slug': ('title',)}
    
    # Añadimos un buscador por título para cuando tengas muchos posts
    search_fields = ['title']