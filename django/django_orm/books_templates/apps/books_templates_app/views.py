from django.shortcuts import render, redirect
from . models import  Book, Author
from datetime import datetime

# Create your views here.
def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books_templates_app/index.html', context)

def authors(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'books_templates_app/authors.html', context)

def showbook(request, id):
    this_book = Book.objects.get(id=id)
    authors_of_book = this_book.authors.all()
    context = {
        'book':this_book,
        'authors': authors_of_book,
        'all_authors': Author.objects.all()
    }
    return render(request, 'books_templates_app/book_page.html', context)

def showauthor(request, id):
    this_author = Author.objects.get(id=id)
    book_authors = this_author.books.all()
    context = {
        'author':this_author,
        'books': book_authors,
        'all_books': Book.objects.all()
    }
    return render(request, 'books_templates_app/author_page.html', context)


def addbook(request):
    if request.method == 'POST':
        Book.objects.create(title=request.POST['book'], desc=request.POST['desc'])
    return redirect('/')

def addauthor(request):
    if request.method == 'POST':
        Author.objects.create(first_name=request.POST['first_name'],last_name = request.POST['last_name'], notes=request.POST['notes'])
    return redirect('/authors')

def addauthor_tobooks(request, id):
    if request.method == 'POST':
        print('-------')
        author = Author.objects.get(id=request.POST['author'])
        author.books.add(Book.objects.get(id=id))
        author.save()
        return redirect('/books/' + id)
####
def addbook_toauthors(request, id):
    if request.method == 'POST':
        print('-------')
        book = Book.objects.get(id=request.POST['book'])
        book.authors.add(Author.objects.get(id=id))
        book.save()
        return redirect('/author_page/' + id)