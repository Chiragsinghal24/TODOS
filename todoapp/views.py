from django.shortcuts import render,redirect
from .models import Mytodo
from .forms import Todoform
from django.contrib.auth.models import User
from django.http import HttpResponse 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def alltodos(request):
    tasks = Mytodo.objects.all()
    form = Todoform()
    if request.method == 'POST':
        form = Todoform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"alltodo.html",{'tasks':tasks,'form':form})

def deleteItem(request,pk):
    task = Mytodo.objects.get(id=pk)
    task.delete()
    return redirect('alltodos')

def updateItem(request, pk):
    todo = Mytodo.objects.get(id=pk)
    updateform = Todoform(instance = todo)
    if request.method == 'POST':
        updateform = Todoform(request.POST,instance=todo)
        if updateform.is_valid():
            updateform.save()
            return redirect('alltodos')
    return render(request,'updateItem.html',{'todo':todo,'updateform':updateform})

def Signuppage(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your Password doesnt match")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login') 
    return render(request,'signup.html')

def Logoutpage(request):
    logout(request)
    return redirect('login')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/todo/')
        else:
            return HttpResponse("user name or password is incorrect")
        
 
    return render(request,'login.html')


