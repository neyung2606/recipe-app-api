from rest_framework import routers
from posts.views import PostsViewSet

app_name = "posts"
router = routers.SimpleRouter(trailing_slash=False)

router.register(r"", viewset=PostsViewSet, basename="Posts")

urlpatterns = router.urls
