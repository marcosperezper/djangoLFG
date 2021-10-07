from django.urls import include, path, re_path
from rest_framework import routers
from .views import VideogameViewSet, GamerViewSet, PartyViewSet, MessageViewSet, welcome, MessageListView, GamerDetailView

router = routers.DefaultRouter()
router.register(r'videogames', VideogameViewSet, basename="videogames")
router.register(r'parties', PartyViewSet, basename="parties")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('welcome/', welcome),
    re_path('^party/(?P<party_id>[^/.]+)/messages/$', MessageListView.as_view(), name='party-message-list'),
    re_path('^gamer/(?P<username>[^/.]+)/$', GamerDetailView.as_view(), name='gamer'),
]
