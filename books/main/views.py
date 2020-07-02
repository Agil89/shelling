from django.shortcuts import render
from main.models import Book,Author,Category
from django.db.models import Q


def get_info(request):
    all_info = Book.objects.all()
    cheaper_books = Book.objects.filter(price__lte=15)
    twentys_authors = Author.objects.filter(date_of_birthday__year__lte=2000)
    book_author_with_a=Book.objects.filter(Q(title__icontains='a')| Q(category__title__icontains='a'))
    dan_defo = Author.objects.filter(fullname='Daniel Defo')
    not_british = Author.objects.exclude(nationality='British')
    start_with_D = Book.objects.filter(author__fullname__startswith='D')
    males = Book.objects.filter(author__gender='mr')
    title_with_e = Book.objects.filter(category__title__endswith='e')
    pk_three= Book.objects.filter(pk='3')
    not_related = Category.objects.filter(books__isnull=True)
    context = {
        'information':all_info,
        'cheaper_books':cheaper_books,
        'twentys_authors':twentys_authors,
        'book_author_with_a':book_author_with_a,
        'dan_defo':dan_defo,
        'not_british':not_british,
        'start_with_D':start_with_D,
        'males':males,
        'title_with_e':title_with_e,
        'pk_three':pk_three,
        'not_related':not_related
    }
    return render(request,'index.html',context)

