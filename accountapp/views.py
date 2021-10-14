from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):

    if request.method == "POST":
        return render(request, 'accountapp/hello_world.html', context={'post' : "이게 작동 된다"})

    return render(request, 'accountapp/hello_world.html', context={})