# library/models.py
from django.db import models

class Student(models.Model):
    student_account = models.CharField(max_length=20, primary_key=True)                  # 学生账户号
    student_password = models.CharField(max_length=20)                                   # 学生密码
    student_name = models.CharField(max_length=20)                                       # 学生姓名
    student_email = models.CharField(max_length=30, unique=True, null=True, blank=True)  # 邮箱
    student_phone = models.CharField(max_length=20, null=True, blank=True)               # 电话

    class Meta:
        db_table = 'student'
        managed = False  # Django不管理此表

    def __str__(self):
        return self.student_name


class Administrator(models.Model):
    admin_account = models.CharField(max_length=20, primary_key=True)                    # 管理员账户号
    admin_password = models.CharField(max_length=20)                                     # 管理员密码
    admin_name = models.CharField(max_length=20)                                         # 管理员姓名
    admin_email = models.CharField(max_length=30, unique=True, null=True, blank=True)    # 邮箱
    admin_phone = models.CharField(max_length=20, null=True, blank=True)                 # 电话

    class Meta:
        db_table = 'administrator'
        managed = False  # Django不管理此表

    def __str__(self):
        return self.admin_name


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)                                    # 图书编号
    book_title = models.CharField(max_length=100)                                   # 图书标题
    book_author = models.CharField(max_length=100)                                  # 作者
    book_publisher = models.CharField(max_length=100, null=True, blank=True)        # 出版社
    book_year = models.IntegerField(null=True, blank=True)                          # 出版年份
    isbn = models.CharField(max_length=13, null=True, blank=True)                   # 国际标准书号
    book_state = models.CharField(max_length=10, default='未借出')                  # 借阅状态

    class Meta:
        db_table = 'book'
        managed = False  # Django不管理此表

    def __str__(self):
        return self.book_title


class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)                                                   # 借阅编号
    book = models.ForeignKey(Book, on_delete=models.CASCADE, db_column='book_id')                  # 图书编号
    student = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='student_account')    # 学生账户号
    borrow_date = models.DateField(null=True, blank=True)                                          # 借阅日期
    due_date = models.DateField(null=True, blank=True)                                             # 应还日期
    return_date = models.DateField(null=True, blank=True)                                          # 归还日期

    class Meta:
        db_table = 'loan'
        managed = False  # Django不管理此表

    def __str__(self):
        return f"Loan {self.loan_id}: {self.book.book_title} by {self.student.student_name}"
