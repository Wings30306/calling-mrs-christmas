from django.shortcuts import render

# Create your views here.
def index_page(request):
    template_name = "main.html"
    return render(request, template_name)