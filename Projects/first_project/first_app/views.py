from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<h1>H1 paragraph</h1> <hr> <h2>H2 paragraph</h2>")
    insert_dict = {'insert_me' : 'Example text inserted into index page!'}
    return render(request, 'index.html', context=insert_dict)

def content(request):
    # return HttpResponse("<h1>This is an example content page</h2>")
    insert_dict = {'insert_me' : 'Example text inserted into content page!'}
    return render(request, 'first_app/content.html', context=insert_dict)