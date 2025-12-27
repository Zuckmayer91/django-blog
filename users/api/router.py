from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Ruta para hacer LOGIN (devuelve Access y Refresh token)
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Ruta para renovar el Access Token cuando se venza
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]