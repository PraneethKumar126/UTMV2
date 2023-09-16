from django.shortcuts import render,redirect
from .models import *
# Create your views here.
import random
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
# def index(request,hashcode):
    # return render(request,'index.html',{'hashcode':hashcode})
def shorten_link(request):
    if request.method=='POST':
        link = request.POST.get('link')
        hashcode = "".join([chr(random.randrange(65,122)) for i in range(15)])
        print(hashcode)
    # Save the link and hashcode to the database
        link_object = HashTable.objects.create(link=link, hashCode=hashcode)
    # return redirect(f'/{hashcode}')
        # return HttpResponse('''<a href="{% url 'decode' %}">Shorten</a>'''+"<h1>{}</h1>".format(hashcode))
        return render(request,'index.html',context={'hashcode':hashcode})
    return render(request,"home.html")


def decode(request):
    if request.method=='POST':
        hashcode=request.POST.get('hashcode')
        link=HashTable.objects.get(hashCode=hashcode).link
        HashTable.objects.get(hashCode=hashcode).delete()
        return redirect(link)
    
    return render(request,'result.html')

