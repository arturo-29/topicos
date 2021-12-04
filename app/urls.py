from rest_framework import routers
from .viewset import *

router = routers.SimpleRouter()
router.register('api/personas', PersonaViewset)
router.register('api/matriculas', MatriculaViewset)

urlpatterns = router.urls