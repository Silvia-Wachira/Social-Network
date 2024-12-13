from rest_framework import routers
from core.user.viewsets import UserViewSet

router = routers.SimpleRouter()

urlpatterns = [
    *router.urls,
]