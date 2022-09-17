import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import CustomerUser


# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'study/signup.html')
    elif request.method == "POST":
        context = {}
        user_id = request.POST.get('user_id',None)
        passwd = request.POST.get('passwd', None)
        passwd2 = request.POST.get('passwd2', None)
        email = request.POST.get('email', None)
        # birth = request.POST["birth"]
        # phone = request.POST["phone"]
        if not (user_id and passwd and passwd2 and email):
            context['error'] = "빈칸없이 입력해주세요."
        elif passwd != passwd2:
            context['error'] = "비밀번호가 다릅니다."
        else:
            user = CustomerUser(
                userid = user_id,
                passwd = make_password(passwd),
                email = email,
            )
            user.save()

        return render(request, 'study/signup.html', context)

def user_login(request):
    if request.method == "GET":
        return render(request, 'study/login.html')
    else:
        context = {}

        user_id = request.POST.get('user_id')
        passwd = request.POST.get('passwd')

        if not (user_id and passwd):
            context['error'] = "빈칸없이 입력해주세요."
        else:
            user = CustomerUser.objects.get(userid = user_id)
            if check_password(passwd, user.passwd):
                request.session['user']=user.id
                return redirect('/')
            else:
                context['error'] = "비밀번호가 틀렸습니다."
    return render(request, 'study/login.html', context)

def user_logout(request):
    if request.session['user']:
        del(request.session['user'])
    return redirect('/account/login')

def home(request):
    user_pk = request.session.get('user')
    username = {}
    if user_pk:
        user = CustomerUser.objects.get(pk=user_pk)
        username['user_id'] = user.userid
        return render(request, 'base.html', username)

    return HttpResponse("로그인 성공")


