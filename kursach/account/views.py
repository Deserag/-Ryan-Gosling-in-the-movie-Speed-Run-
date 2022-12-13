from django.shortcuts import render
from account.models import account
def accounts(request):
      print(str(request.path).find('_'))
      data = account.objects.filter(ID_Game = str(request.path)[str(request.path).find('_')+1:]) 
      gam= {'account':data}
      
      return render(request,'bued.html',gam)