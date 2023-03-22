from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'cms/home_page.html')