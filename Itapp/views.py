from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')


def abo(request):
    return render(request, 'about.html')


def ser(request):
    return render(request, 'service.html')



def pro(request):
    return render(request, 'project.html')



def blo(request):
    return render(request, 'blog.html')



def tea(request):
    return render(request, 'team.html')



def tes(request):
    return render(request, 'testimonial.html')



def four(request):
    return render(request, '404.html')



def con(request):
    return render(request, 'contact.html')
