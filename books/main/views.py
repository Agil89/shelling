from django.shortcuts import render
from main.models import Book,Author,Category
from django.db.models import Q,F
from django.db.models import Avg,Sum

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
    # Book.objects.filter(page_count__lte=300).update(page_count=350)
    updated_books = Book.objects.all()
    Book.objects.filter(author__gender='ms').update(price=13.8)
    updated_female_books = Book.objects.all()
    Book.objects.filter(page_count__gte=500).delete()
    books_after_deleted = Book.objects.all()
    Author.objects.filter(fullname__contains='a').order_by('date_of_birthday')
    Book.objects.all().distinct()
    author_for_new_book= Author.objects.filter(pk=3).first()
    new_cate_for_book = Category.objects.filter(pk=2)
    if author_for_new_book and new_cate_for_book:
        book,created = Book.objects.get_or_create(author=author_for_new_book,title='JOn lenon',image='img.png',
                                                   description='hello',price='15',page_count='50')
        for cat in new_cate_for_book:
            book.category.add(cat)
    book_count = Book.objects.filter(category__title='Novel').count()
    Book.objects.all().first()
    Book.objects.all().last()
    Book.objects.all().order_by('-id')[:3]
    Book.objects.all().aggregate(Avg('price'))
    Book.objects.all().aggregate(Sum('price'))
    Book.objects.filter(price__lte=F('page_count')/10)
    print(Book.objects.filter(Q(page_count__lte='200') | Q(price__gte='15')))
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
        'not_related':not_related,
        'updated_books':updated_books,
        'updated_female_books':updated_female_books,
        'books_after_deleted':books_after_deleted,
    }
    return render(request,'index.html',context)

