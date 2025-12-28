"""
URL configuration for my_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.conf import settings # IMPORTANTE
from django.conf.urls.static import static # IMPORTANTE

from posts.api.router import router_post
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="API Blog Profesional",  # <--- Cambia esto
      default_version='v1',
      description="Documentación de los endpoints para el sistema de Blog", # <--- Cambia esto
      terms_of_service="", # Puedes dejarlo vacío
      contact=openapi.Contact(email="tu-email@dominio.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
)


from django.views.generic import RedirectView # Añade este import

urlpatterns = [
    # Añade esta línea al principio de urlpatterns:
    path('', RedirectView.as_view(url='/docs/', permanent=False)),
    
    path('admin/', admin.site.urls),  
    path('api/', include(router_post.urls)), 
    # ... resto de tus urls
]
urlpatterns = [
   path('admin/', admin.site.urls),  
   path('api/', include(router_post.urls)), 
   path('api/', include('users.api.router')), 
   path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# --- ESTO ES LO QUE DEBES AGREGAR ---
# Permite que Django sirva archivos estáticos y de media durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)