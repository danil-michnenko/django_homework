from django.shortcuts import render

# Create your views here.

def showBook(request):
    return render(request, "Book/book.html")