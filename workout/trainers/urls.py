from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import WorkoutList,WorkoutDetailView

# router = SimpleRouter()
# router.register('workouts', WorkoutViewset)
# router.register('blog', BlogViewset)

# urlpatterns = router.urls

urlpatterns = [ 
    path('workouts/',WorkoutList.as_view(),name='workouts'),
    path('workouts/<int:pk>/',WorkoutDetailView.as_view(),name='workouts')
]
