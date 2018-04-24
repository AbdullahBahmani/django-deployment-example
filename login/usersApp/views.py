from django.shortcuts import render
from .models import Authors,Books
from .forms import NewBookForm


# Create your views here.
def bookList(request):
    bookLists=Books.objects.order_by('bookId')
    my_dict={'bookLists':bookLists}
    return render(request,'userApp/Booklist.html',my_dict)
