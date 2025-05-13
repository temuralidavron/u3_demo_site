from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render,redirect

from book.form import BookForm
from book.models import Book, Author
from book_u3 import settings
from .utils import muyasar_perm,admin_perm

# @permisson_required()
# @admin_perm
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm(request.POST)
    return render(request, 'book/book_form.html', {'form': form})





def book_list(request):
    books = Book.objects.all()
    q=request.GET.get('q')
    if q:
        books = books.filter(Q(title__icontains=q) | Q(description__icontains=q))
    else:
        books = books.all()
    books = books.order_by('title')
    paginator = Paginator(books, 2)
    page = request.GET.get('page',1)
    books = paginator.get_page(page)
    return render(request, 'book/book_list.html', {'books': books})

# @permission_required("book.view_book",raise_exception=True)
def book_detail(request,pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})

def book_edit(request,pk):
    book = Book.objects.get(pk=pk)

    if request.method == "POST":
        form=BookForm(request.POST ,instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form=BookForm(instance=book)
    return render(request, 'book/book_form.html', {'form': form})


def book_delete(request,pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book-list')
    else:
        return render(request, 'book/book_delete.html', {'book': book})



from django.core.mail import send_mail, EmailMultiAlternatives
from django.http import HttpResponse

def send_email_view(request,subject, from_email, to_email,):
    send_mail(
        subject='Salom do‘stim!',
        message='Bu test xabari. Django orqali email jo‘natildi!',
        from_email='aliyer.temur95@gmail.com',
        recipient_list=['aliyevtemur562@gmail.com','farhadkuddi8@gmail.com','akobirroziqulov4@gmail.com'],  # bu joyga qaysi emailga jo'natmoqchi bo‘lsangiz shuni yozing
        fail_silently=False,
    )
    return HttpResponse("Email (konsolga) yuborildi!")


from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.http import HttpResponse

# def send_html_view(request,subject, to_email,code):
#     subject = subject
#     from_email = settings.EMAIL_HOST_USER
#     to_email =to_email
#     text_content =code
#     html_content = f"<h1>Salom</h1><p>Bu <strong>HTML</strong> matn.{text_content}</p>"
#
#     email = EmailMultiAlternatives(
#         subject=subject,
#         body=text_content,
#         from_email=from_email,
#         to=to_email
#     )
#     email.attach_alternative(html_content, "text/html")
#     email.send()
#
#     return HttpResponse("Email yuborildi!")
#
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.http import HttpResponse

def send_html_view(request, subject, to_email, code,username):
    from_email = settings.EMAIL_HOST_USER
    text_content = code
    subject=subject

    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px;">
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h2 style="color: #333333;">Salom!</h2>
            <p style="font-size: 16px; color: #555555;">Parolni tiklash uchun quyidagi koddan foydalaning:</p>
            <div style="background-color: #f0f0f0; padding: 15px; border-radius: 5px; font-size: 20px; text-align: center; font-weight: bold; color: #2c3e50;">
                {code}
            </div>
            <p style="font-size: 16px; color: #555555; margin-top: 20px;">Yoki quyidagi tugmani bosib parolingizni tiklashingiz mumkin:</p>
            <a href="http://127.0.0.1:8000/accounts/reset/?name={username}" 
            <b>{code}</b>
               style="display: inline-block; padding: 12px 20px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px; font-weight: bold;">
               Parolni tiklash
            </a>
            <p style="font-size: 14px; color: #999999; margin-top: 30px;">Agar bu siz emas bo‘lsangiz, bu xabarni e'tiborsiz qoldiring.</p>
        </div>
    </body>
    </html>
    """

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=from_email,
        to=[to_email] if isinstance(to_email, str) else to_email
    )
    email.attach_alternative(html_content, "text/html")
    email.send()

    return HttpResponse("Email yuborildi!")


