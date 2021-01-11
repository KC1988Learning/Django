from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'title' : 'Colorful homepage'}
    return render(request, 'index.html', context=context_dict)

def content(request):
    context_dict = {'title' : 'Meaningful content'}
    return render(request, 'second_app/content.html', context=context_dict)