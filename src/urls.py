from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from attractions.views import AttractionsViewSet

router = routers.DefaultRouter()
router.register(r'attractions', AttractionsViewSet, base_name="attractions")

urlpatterns = [
    url('', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
