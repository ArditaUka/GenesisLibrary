from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, Book
import bcrypt


# Create your views here.
def index(request):
    query = request.GET.get("q")
    if query:
        queryset_list = Book.objects.all().filter(title_icontains=query)
    context = {
        "book_list": queryset_list
    }
    return render(request, "index.html", context)
def display_login(request):
    return render(request, 'signin.html')

def display_register(request):
    return render (request, 'register.html')

def register(request):
    errors = User.objects.validator(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/display_register')
    else:
        print(request.POST['first_name'])
        hash_pw = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()).decode()
        
        user = User.objects.create(first_name = request.POST['first_name'], last_name=request.POST['last_name'], email = request.POST['email'], password=hash_pw)

        request.session["uid"] = user.id
        if 'redirect' in request.session:
                redirect_url = request.session['redirect']
                del request.session['redirect']
                return redirect(f'/{redirect_url}')

        return redirect('/')


def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if len(user)>0:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['uid'] = logged_user.id
            if 'redirect' in request.session:
                redirect_url = request.session['redirect']
                del request.session['redirect']
                return redirect(f'/{redirect_url}')
            return redirect('/')
        else:
            messages.error(request,"Email and password did not match")
    else:
        messages.error(request,"Email address is not registered yet.")
    return redirect('/display_login')

def logout(request):
    del request.session['uid']
    return redirect('/')

def about(request):
    return render(request,"about.html")

def books_list(request):
    query = request.GET.get("q")
    if query:
        queryset_list = Book.objects.all().filter(title_icontains=query)
        context = {
            "book_list": queryset_list
        }
    return render(request, "index.html", context)