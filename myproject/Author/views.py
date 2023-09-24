from django.shortcuts import render

# Create your views here.

def showAuthor(request):
    return render(request, "Author/author.html")