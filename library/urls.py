# library/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 登录与注册
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # 学生首页与功能
    path('student/home/', views.student_home, name='student_home'),
    path('profile/', views.view_profile, name='view_profile'),
    path('student/loans/', views.view_loan_records, name='view_loan_records'),
    path('books/', views.view_all_books, name='view_all_books'),
    path('books/borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('books/search/', views.search_books_view, name='search_books'),
    path('loans/return/<int:loan_id>/', views.return_book, name='return_book'),
    path('loans/extend/<int:loan_id>/', views.extend_loan, name='extend_loan'),

    # 管理员首页与功能
    path('admin/home/', views.admin_home, name='admin_home'),
    path('admin/students/', views.admin_view_students, name='admin_view_students'),
    path('admin/students/add/', views.admin_add_student, name='admin_add_student'),
    path('admin/students/edit/<str:student_account>/', views.admin_edit_student, name='admin_edit_student'),
    path('admin/students/delete/<str:student_account>/', views.admin_delete_student, name='admin_delete_student'),
    path('admin/students/<str:student_account>/loans/', views.admin_view_student_loans, name='admin_view_student_loans'),
    path('admin/books/', views.admin_view_books, name='admin_view_books'),
    path('admin/books/add/', views.admin_add_book, name='admin_add_book'),
    path('admin/books/edit/<int:book_id>/', views.admin_edit_book, name='admin_edit_book'),
    path('admin/books/delete/<int:book_id>/', views.admin_delete_book, name='admin_delete_book'),
    path('admin/books/search/', views.admin_search_books_view, name='admin_search_books'),
    path('admin/add_admin/', views.admin_add_admin, name='admin_add_admin'),
]
