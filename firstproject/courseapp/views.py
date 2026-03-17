from django.shortcuts import render

# Create your views here.
def django_view(request):
    student={'name':'Arghya','roll-no':12345,'gender':'male'}
    return render(request,"courseapp/django.html",{'dic':student})