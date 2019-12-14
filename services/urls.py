from django.urls import path
from .views import ServiceCategoryListView, service_list_by_category_view, ServiceDetailView

app_name = "services"
urlpatterns = [
    path('', ServiceCategoryListView.as_view(), name="services_list"),
    path('<slug:category>', service_list_by_category_view, name="services_list_by_cat"),
    path('<int:pk>', ServiceDetailView.as_view(), name="service_detail"),
]
