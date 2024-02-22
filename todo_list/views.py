from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def blog(request):
    return HttpResponse("Hello this is a view inside the BLOG WHOOOOOOOOOOOOOOOOOOOH!")

def contacts(request):
    return HttpResponse("CONTACTS!!!!")

def about(request):
    context ={
        'firstname': 'Clem',
        'secondname': 'fandago',
        'exam_results': [64,78,89],
        'subjects':{'ALevel':'Maths','TLevel':'Digital'}

    }
    return render(request, 'aboutme.html', context)