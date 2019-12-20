from django.urls import path
from .views import (LocationListView,
                    LocationDetailView,
                    LocationCreateView,
                    LocationUpdateView,
                    LocationDeleteView)

app_name = "contact"
urlpatterns = [
    path('', LocationListView.as_view(), name="contact"),
    path('<int:pk>', LocationDetailView.as_view(), name="location"),
    path('create', LocationCreateView.as_view(), name="create_location"),
    path('<int:pk>/update', LocationUpdateView.as_view(), name="update_location"),
    path('<int:pk>/delete', LocationDeleteView.as_view(), name="delete_location"),
]
