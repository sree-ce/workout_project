from django.urls import re_path
from .views import *
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('program',ProgramViewset )
urlpatterns = router.urls

