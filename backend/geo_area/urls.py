from django.urls import path

from .views import GeoAreaViewSet

app_name = "geo_area"


urlpatterns = [
    path("", GeoAreaViewSet.as_view({"get": "list"}), name="georea-list"),
    path(
        "<int:pk>/",
        GeoAreaViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="georea-detail",
    ),
]
