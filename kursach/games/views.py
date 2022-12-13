from django.shortcuts import render
from django.views.generic import ListView

from games.models import games

def osnos(request):
      data = games.objects.all()
      gam= {'game':data}
      return render(request,'contact_list.html',gam)