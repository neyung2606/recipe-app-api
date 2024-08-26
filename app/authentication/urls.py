from rest_framework import routers
from authentication.views import AuthViewSet


app_name = "auth"

router = routers.SimpleRouter()
router.register(r"", AuthViewSet, basename="authentication")

urlpatterns = router.urls
