# library/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import (
    LoginForm, RegisterForm, ProfileForm, AdminRegisterForm,
    BookForm, AdminAddStudentForm, AdminEditStudentForm
)
from .models import Student, Administrator, Book, Loan
from .decorators import student_required, admin_required
from django.db import connection
from datetime import timedelta
from django.utils import timezone


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            account_type = form.cleaned_data['account_type']
            account = form.cleaned_data['account']
            raw_password = form.cleaned_data['password']

            if account_type == 'student':
                try:
                    user = Student.objects.get(student_account=account)
                except Student.DoesNotExist:
                    messages.error(request, '学生账户不存在')
                    return render(request, 'library/login.html', {'form': form})

                if user.student_password != raw_password:
                    messages.error(request, '密码错误')
                    return render(request, 'library/login.html', {'form': form})

                request.session['account'] = account
                request.session['account_type'] = 'student'

                return redirect('student_home')

            elif account_type == 'admin':
                try:
                    user = Administrator.objects.get(admin_account=account)
                except Administrator.DoesNotExist:
                    messages.error(request, '管理员账户不存在')
                    return render(request, 'library/login.html', {'form': form})

                if user.admin_password != raw_password:
                    messages.error(request, '密码错误')
                    return render(request, 'library/login.html', {'form': form})

                request.session['account'] = account
                request.session['account_type'] = 'admin'

                return redirect('admin_home')

    else:
        form = LoginForm()

    return render(request, 'library/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            account = form.cleaned_data['account']
            raw_password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            if Student.objects.filter(student_account=account).exists():
                messages.error(request, '账户号已存在，请选择其他账户号。')
                return render(request, 'library/register.html', {'form': form})

            new_student = Student(
                student_account=account,
                student_password=raw_password,
                student_name=name,
                student_email=email if email else None,
                student_phone=phone if phone else None
            )
            new_student.save()

            messages.success(request, '注册成功！请登录。')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'library/register.html', {'form': form})

@student_required
def student_home(request):
    account = request.session.get('account')
    try:
        user = Student.objects.get(student_account=account)
    except Student.DoesNotExist:
        messages.error(request, '用户不存在。')
        return redirect('login')
    return render(request, 'library/student_home.html', {'user_name': user.student_name})

@admin_required
def admin_home(request):
    account = request.session.get('account')
    try:
        user = Administrator.objects.get(admin_account=account)
    except Administrator.DoesNotExist:
        messages.error(request, '用户不存在。')
        return redirect('login')
    return render(request, 'library/admin_home.html', {'user_name': user.admin_name})

@student_required
def view_profile(request):
    account = request.session.get('account')
    student = get_object_or_404(Student, student_account=account)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=student)
        if form.is_valid():
            profile = form.save(commit=False)
            new_password = form.cleaned_data.get('password')
            if new_password:
                profile.student_password = new_password
            profile.save()
            messages.success(request, '个人资料更新成功。')
            return redirect('view_profile')
    else:
        form = ProfileForm(instance=student)
    return render(request, 'library/view_profile.html', {'form': form})

@student_required
def view_loan_records(request):
    account = request.session.get('account')
    loans = Loan.objects.filter(student__student_account=account).select_related('book')
    return render(request, 'library/view_loan_records.html', {'loans': loans})

@student_required
def view_all_books(request):
    books = Book.objects.all()
    return render(request, 'library/view_all_books.html', {'books': books})

@admin_required
def admin_view_students(request):
    students = Student.objects.all()
    return render(request, 'library/admin_view_students.html', {'students': students})

@admin_required
def admin_add_student(request):
    if request.method == 'POST':
        form = AdminAddStudentForm(request.POST)
        if form.is_valid():
            account = form.cleaned_data['account']
            raw_password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            if Student.objects.filter(student_account=account).exists():
                messages.error(request, '该学生账户已存在')
                return render(request, 'library/admin_add_student.html', {'form': form})

            new_student = Student(
                student_account=account,
                student_password=raw_password,
                student_name=name,
                student_email=email if email else None,
                student_phone=phone if phone else None
            )
            new_student.save()

            messages.success(request, '学生账户添加成功')
            return redirect('admin_view_students')
    else:
        form = AdminAddStudentForm()
    return render(request, 'library/admin_add_student.html', {'form': form})

@admin_required
def admin_edit_student(request, student_account):
    student = get_object_or_404(Student, student_account=student_account)
    if request.method == 'POST':
        form = AdminEditStudentForm(request.POST)
        if form.is_valid():
            student.student_name = form.cleaned_data['name']
            student.student_email = form.cleaned_data['email'] if form.cleaned_data['email'] else None
            student.student_phone = form.cleaned_data['phone'] if form.cleaned_data['phone'] else None
            form_password = request.POST.get('password', '')
            if form_password:
                student.student_password = form_password
            student.save()
            messages.success(request, '学生信息更新成功')
            return redirect('admin_view_students')
    else:
        initial_data = {
            'name': student.student_name,
            'email': student.student_email,
            'phone': student.student_phone,
        }
        form = AdminEditStudentForm(initial=initial_data)
    return render(request, 'library/admin_edit_student.html', {'form': form, 'student_account': student_account})

@admin_required
def admin_delete_student(request, student_account):
    student = get_object_or_404(Student, student_account=student_account)
    student.delete()
    messages.success(request, '学生账户已删除')
    return redirect('admin_view_students')

@admin_required
def admin_view_books(request):
    books = Book.objects.all()
    return render(request, 'library/admin_view_books.html', {'books': books})

@admin_required
def admin_add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book_title = form.cleaned_data['book_title']
            book_author = form.cleaned_data['book_author']
            book_publisher = form.cleaned_data['book_publisher']
            book_year = form.cleaned_data['book_year']
            isbn = form.cleaned_data['isbn']
            book_state = form.cleaned_data['book_state']

            new_book = Book(
                book_title=book_title,
                book_author=book_author,
                book_publisher=book_publisher if book_publisher else None,
                book_year=book_year if book_year else None,
                isbn=isbn if isbn else None,
                book_state=book_state if book_state else None
            )
            new_book.save()
            messages.success(request, '图书添加成功')
            return redirect('admin_view_books')
    else:
        form = BookForm()
    return render(request, 'library/admin_add_book.html', {'form': form})

@admin_required
def admin_edit_book(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book.book_title = form.cleaned_data['book_title']
            book.book_author = form.cleaned_data['book_author']
            book.book_publisher = form.cleaned_data['book_publisher'] if form.cleaned_data['book_publisher'] else None
            book.book_year = form.cleaned_data['book_year'] if form.cleaned_data['book_year'] else None
            book.isbn = form.cleaned_data['isbn'] if form.cleaned_data['isbn'] else None
            book.book_state = form.cleaned_data['book_state'] if form.cleaned_data['book_state'] else None
            book.save()
            messages.success(request, '图书信息更新成功')
            return redirect('admin_view_books')
    else:
        initial_data = {
            'book_title': book.book_title,
            'book_author': book.book_author,
            'book_publisher': book.book_publisher,
            'book_year': book.book_year,
            'isbn': book.isbn,
            'book_state': book.book_state,
        }
        form = BookForm(initial=initial_data)
    return render(request, 'library/admin_edit_book.html', {'form': form, 'book_id': book_id})

@admin_required
def admin_delete_book(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)
    book.delete()
    messages.success(request, '图书已删除')
    return redirect('admin_view_books')

@admin_required
def admin_add_admin(request):
    if request.method == 'POST':
        form = AdminRegisterForm(request.POST)
        if form.is_valid():
            account = form.cleaned_data['account']
            raw_password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            if Administrator.objects.filter(admin_account=account).exists():
                messages.error(request, '管理员账户号已存在，请选择其他账户号。')
                return render(request, 'library/admin_add_admin.html', {'form': form})

            new_admin = Administrator(
                admin_account=account,
                admin_password=raw_password,
                admin_name=name,
                admin_email=email if email else None,
                admin_phone=phone if phone else None
            )
            new_admin.save()
            messages.success(request, '管理员账户添加成功。')
            return redirect('admin_home')
    else:
        form = AdminRegisterForm()
    return render(request, 'library/admin_add_admin.html', {'form': form})

@admin_required
def admin_view_student_loans(request, student_account):
    student = get_object_or_404(Student, student_account=student_account)
    loans = Loan.objects.filter(student=student).select_related('book')
    return render(request, 'library/admin_view_student_loans.html', {'student': student, 'loans': loans})

def logout_view(request):
    request.session.flush()  # 清除所有会话数据
    messages.success(request, '成功登出。')
    return redirect('login')

@student_required
def borrow_book(request, book_id):
    student_account = request.session.get('account')
    book = get_object_or_404(Book, book_id=book_id)
    if book.book_state == '已借出':
        messages.error(request, '此图书已被借出。')
        return redirect('view_all_books')

    # 创建借阅记录
    new_loan = Loan.objects.create(
        book=book,
        student=Student.objects.get(student_account=student_account),
        borrow_date=timezone.now().date(),
        due_date=(timezone.now().date() + timedelta(days=30))
    )
    # 更新图书状态
    book.book_state = '已借出'
    book.save()

    messages.success(request, '借阅成功！请按时归还。')
    return redirect('view_all_books')

@student_required
def return_book(request, loan_id):
    loan = get_object_or_404(Loan, loan_id=loan_id, student__student_account=request.session.get('account'))
    if loan.return_date is not None:
        messages.error(request, '此图书已归还。')
        return redirect('view_loan_records')

    # 归还操作
    loan.return_date = timezone.now().date()
    loan.save()

    # 更新图书状态为“未借出”
    loan.book.book_state = '未借出'
    loan.book.save()

    messages.success(request, '归还成功！')
    return redirect('view_loan_records')

@student_required
def extend_loan(request, loan_id):
    loan = get_object_or_404(Loan, loan_id=loan_id, student__student_account=request.session.get('account'))
    if loan.return_date is not None:
        messages.error(request, '此图书已归还，无法延期。')
        return redirect('view_loan_records')

    # 延期7天
    loan.due_date += timedelta(days=7)
    loan.save()

    messages.success(request, f'延期成功！新的应还日期为 {loan.due_date}。')
    return redirect('view_loan_records')

def search_books_view(request):
    query = request.GET.get('q')
    if (query):
        books = Book.objects.filter(book_title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'library/search_books.html', {'books': books, 'query': query})

@admin_required
def admin_search_books_view(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(book_title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'library/admin_search_books.html', {'books': books, 'query': query})
