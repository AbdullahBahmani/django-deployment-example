from django.shortcuts import render
from usersApp.forms import NewBookForm


def index(request):
    form= NewBookForm()
    return render(request, 'index.html',{'form':form})
