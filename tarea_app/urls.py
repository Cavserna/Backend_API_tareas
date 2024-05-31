from rest_framework import routers
from .views import TareaViewSet

# módulo propio de rest framework para que genere las rutas aútomáticamente
router = routers.DefaultRouter()

router.register('api/tareas', TareaViewSet, 'tareas')

urlpatterns = router.urls
