from django.conf.urls import patterns, url, include
from rest_framework import routers
from yelo import views

router = routers.DefaultRouter()
router.register(r'elos', views.EloViewSet)
router.register(r'matches', views.MatchViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns(
    '',
    url(r'^$', views.index),
    url(r'^record_match$', views.record_match),
    url(r'^add_player$', views.add_player),
    url(r'^api/', include(router.urls))
)
