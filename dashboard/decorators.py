from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import Group

def get_or_create_editor_admin_group():
    editors_group = Group.objects.get_or_create(name='editors')
    admin_group = Group.objects.get_or_create(name='admin')
    return editors_group[0], admin_group[0]


def admin_and_editor_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        editors_group, admin_group = get_or_create_editor_admin_group()
        
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)

        elif request.user.groups.exists():
            groups = request.user.groups.all()
            
            if editors_group in groups or admin_group in groups:
                return view_func(request, *args, **kwargs)
            
        return HttpResponse('You Not allowed to visit there url')


    return wrapper_func


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        _ , admin_group = get_or_create_editor_admin_group()
        
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)

        elif request.user.groups.exists():
            if admin_group in request.user.groups.all():
                return view_func(request, *args, **kwargs)
            
        return HttpResponse('You Not allowed to visit there url')

    return wrapper_func

