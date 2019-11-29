from django.shortcuts import render

# Create your views here.
def services_list_view(request, *args, **kwargs):
    return render(request, "services_list.html")

def services_detail_view(request, *args, **kwargs):
    return render(request, "services_detail.html")