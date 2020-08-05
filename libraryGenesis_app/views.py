from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, Book
import bcrypt


# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        "books":books
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

def admin(request):
    return render(request,"admin_login.html")

def admin_login(request):
    user = User.objects.filter(email=request.POST['email'])
    if len(user)>0:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            # return HttpResponse(request.POST['email'])
            if request.POST['email'] == "admin@gmail.com":
                request.session['uid'] = logged_user.id
                return redirect('/book')
            else:
                messages.error(request,"Wrong initials for admin")    
        else:
            messages.error(request,"Email and password did not match")
    else:
        messages.error(request,"Email address is not registered yet.")
    return redirect('/admin')



def book(request):
    books=Book.objects.all()
    context = {
        "books":books

    }
    return render(request, "book.html", context)

def new_book(request):
    return render(request, "new_book.html")

def create_book(request):
    
    errors = Book.objects.validator(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request,value)
        
        return redirect('/new_book')
    else:

        title = request.POST['title']
        author = request.POST['author']
        publish_date= request.POST['publish_date']
        genre = request.POST["genre"]
        days_avaliable = request.POST['days_avaliable']
        price = request.POST['price']
        about = request.POST['about']
        
        if len(genre)<1 or genre=="Choose...":
            messages.error(request,"Your book must belong to a genre")
            return redirect('/new_book')
        
        else:
            user = User.objects.get(id=request.session['uid'])
            book = Book.objects.create(title=title, author=author, genre=genre, publish_date=publish_date, price = price, days_avaliable=days_avaliable, about=about)
        
        return redirect('/book')

def edit(request, book_id):
    if 'uid' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['uid'])
    book = Book.objects.get(id=book_id)
    context = {
        'book':book,
        'user':user
    }
    return render(request, 'edit.html', context)

def update(request,book_id):
    errors = Book.objects.validator(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request,value)
        
        return redirect(f'/edit/{book_id}')
    else:
        book = Book.objects.get(id=book_id)
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.publish_date= request.POST['publish_date']
        book.genre = request.POST["genre"]
        book.days_avaliable = request.POST['days_avaliable']
        book.price = request.POST['price']
        book.about = request.POST['about']
        
        if len(book.genre)<1 or book.genre=="Choose...":
            messages.error(request,"Your book must belong to a genre")
            return redirect(f'/edit/{book_id}')
        
        else:
            book.save()
        return redirect('/book')


def delete(request, book_id):
    user = User.objects.get(id=request.session['uid'])
    book = Book.objects.get(id=book_id)
    book.delete()

    return redirect('/book')


def display_genre(request, genre):
    books = Book.objects.filter(genre=genre)
    all_books = Book.objects.all()
    
    context = {
        'genre_books': books,
        'books': all_books
    }
    return render(request,'books_genre.html', context)

def display(request, book_id):
    book = Book.objects.get(id=book_id)
    
    context = {
        'book': book
    }
    return render(request,'display.html', context)

def borrow_info(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        'book': book
    }
    return render(request, 'borrow_info.html', context)

def borrow(request, book_id):
    request.session['redirect'] = (f'borrow_info/{book_id}')
    return redirect('/display_login')

def borrow_book(request, book_id):
    user = User.objects.get(id=request.session['uid'])
    book = Book.objects.get(id=book_id)
    user.books.add(book)
    return redirect('/')

def display_borrowed(request):
    books= Book.objects.all()
    user = User.objects.get(id = request.session['uid'])
    ordered_books = user.books.all()
    context={
        "books": ordered_books
    }
    return render(request,"display_borrowed.html", context)

def return_book(request, book_id):
    user = User.objects.get(id=request.session['uid'])
    book = Book.objects.get(id=book_id)
    user.books.remove(book)
    return redirect('/')