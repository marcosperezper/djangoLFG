from django.urls import include, path, re_path
from rest_framework import routers
from .views import VideogameViewSet, GamerViewSet

router = routers.DefaultRouter()
router.register(r'videogames', VideogameViewSet, basename="videogames")
router.register(r'gamers', GamerViewSet, basename="gamers")

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
