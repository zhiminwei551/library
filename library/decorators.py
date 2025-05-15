from functools import wraps
from django.shortcuts import redirect

def student_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.session.get('account_type') == 'student':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return _wrapped_view

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.session.get('account_type') == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return _wrapped_view
