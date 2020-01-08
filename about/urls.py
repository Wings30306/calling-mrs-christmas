from django.urls import path
from .views import about_view, detail_view, casestudy_list_view

app_name = "about"
urlpatterns = [
    path('', about_view, name="about_list"),
    path('casestudies', casestudy_list_view, name="casestudies"),
    path('<slug:user>', detail_view, name="about_detail"),

]
