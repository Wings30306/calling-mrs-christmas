from django.urls import path
from .views import ServiceCategoryListView, service_list_by_category_view, service_detail_view

app_name = "services"
urlpatterns = [
    path('', ServiceCategoryListView.as_view(), name="services_list"),
    path('<slug:category>', service_list_by_category_view, name="services_list_by_cat"),
    path('detail/<int:primary_key>', service_detail_view, name="service_detail"),
]
