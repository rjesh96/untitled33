from django.shortcuts import render,redirect
from.forms import UserForm
from.models import User

# Create your views here.
def welcome(request):
    return render(request,"welcome.html")

def load_form(request):
    form=UserForm
    return render(request,"index.html",{'form':form})

def add(request):
    form=UserForm(request.POST)
    form.save()
    return redirect('/show')

def show(request):
    user=User.objects.all
    return render(request,"show.html",{'user':user})

def edit(request,id):
    user = User.objects.get(id=id)
    return render(request,"edit.html",{'user':user})


def update(request,id):
    user=User.objects.get(id=id)
    form=UserForm(request.POST,instance=user)
    form.save()
    return redirect('/show')

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/show')

def search(request):
    given_name=request.POST['name']#try it: (uname__iexact=given_name)
    user=User.objects.filter(uname__icontains=given_name)
    return  render(request,"show.html",{'user': user})



