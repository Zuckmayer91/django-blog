
from rest_framework.routers import DefaultRouter
# Cambia PostViewSet por postModelViewSet
from posts.api.views import postModelViewSet 

router_post = DefaultRouter()

# Asegúrate de usar el nuevo nombre aquí también en 'viewset'
router_post.register(prefix='posts', basename='posts', viewset=postModelViewSet)