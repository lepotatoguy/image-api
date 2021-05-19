from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import image
from django.shortcuts import render
from .forms import *
from PIL import Image

# Create your views here.
#This is a basic API made by Django which will printout the resolution of a given picture.

def index(request):
    #params = {'allProds': allProds}
    # if request.method == 'POST':
    #     form = index(request.POST, request.FILES)
  
    #     if form.is_valid():
    #         form.save()
    #         return redirect('success')

    # params = {'allProds': 1}
    #return HttpResponseRedirect('index.html')
    
    return render(request, 'index.html')

def uploadImage(request):
    pic = request.FILES['image']
    print(pic)
    img = image(img= pic)
    img.save()
    img_size = Image.open(pic)
    width, height = img_size.size
    print(width, height)

    #return HttpResponse('hello')
    return JsonResponse({'height': height, 'width': width})