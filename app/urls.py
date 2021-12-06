from rest_framework import routers
from .viewset import *

router = routers.SimpleRouter()
router.register('api/alumnos', AlumnoViewset)
router.register('api/matriculas', MatriculaViewset)
router.register('api/materia', MateriaViewset)
router.register('api/docente', DocenteViewset)
router.register('api/calificacion', CalificacionViewset)

urlpatterns = router.urls