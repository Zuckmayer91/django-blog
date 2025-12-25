from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
class HelloWorld(View):
     def get(self, request):
         data={
             
             'name': 'Agustin Navarro Galdon',
             'years': 28,
             'codes': ['Python','Django','React']
             
             }
         return render(request,'hello_world.html')