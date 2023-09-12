
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

from django.contrib import messages
from App.forms import signUpForm
from .models import Record
from .forms import AddForm

def home(request):
    records=Record.objects.all()



   # check login
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        #authenticate
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Logged In')
            return redirect('home')
        else:
            messages.success(request, 'There Was Error')
    return render(request, 'App/templates/home.html',{'records':records})

def logout_user(request):
    logout(request)
    messages.success(request,'You Have Logged Out...')
    return redirect('home')

def register_user(request):
    if request.method=='POST':
        form=signUpForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(request,username=username,password=password)
            login(request, user)
            messages.success(request, 'You have Successfully registered')
            return redirect('home')
    
    form=signUpForm()
    return render(request,'App/templates/register.html',{'form':form})
    

def customer_record(request,pk):
    if request.user.is_authenticated:
        #look UP records
        customer_record=Record.objects.get(id=pk)
        return render(request,'App/templates/record.html',{'customer_record':customer_record})
    else:
        messages.success(request, 'You Must Be Logged In First')
        return redirect('home')

def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it=Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record Deleted Successfully...')
        return redirect('home')
    else:
        messages.success(request, 'You Must Be Log In First!!')
        return redirect('home')
def add_record(request):
    add=AddForm()
    if request.user.is_authenticated:
        
        if request.method=='POST':
            add=AddForm(request.POST)
            if add.is_valid():
                add.save()
                messages.success(request, "Record Added")
                return redirect('home')
    return render(request, 'App/templates/add_records.html',{'add':add})
def update_record(request,pk):
    
    if request.user.is_authenticated:
        current_record=Record.objects.get(id=pk)
        form=AddForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Updated!')
            return redirect('home')
        return render(request, 'App/templates/update_record.html',{'update':form})
    else:
        messages.success(request, 'Logged In First!')
        return redirect('home')

# from .models import Post    
# from django.shortcuts import render,redirect

# def blog_page(request):
#     post=Post.objects.get(title='abc')
    

#     context={'post':post}

#     return render(request, '/home/tor/Desktop/django/CRM App/App/templates/index.html',{'post':post})

            
    