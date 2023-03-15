from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash, user_logged_out

from django.core.checks import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView

import news
from news.models import New, Category, SubCategory
from .forms import LoginForm, AdminNewsUpdateForm


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username=data['username'],
                                password=data['password']
                                )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    success_url = 'admin_home_page'
                    return redirect(success_url)
                else:
                    return HttpResponse('Sizni hissobingiz faol holatda emas!')
            else:
                return HttpResponse('Login yoki parol xato!')

    else:
        return render(request, 'admin/login.html')

        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'admin/login.html', context)


class AdminHomePageView(ListView):
    model = User
    template_name = 'admin/home.html'
    context_object_name = 'admin_home_page'




def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get("password_old")
        new_password = request.POST.get("password_new1")
        confirmed_new_password = request.POST.get("password_new2")

        if old_password and new_password and confirmed_new_password:
            if request.user.is_authenticated:
                user = User.objects.get(username=request.user.username)
                if not user.check_password(old_password):
                    return HttpResponse(request, "Eski parolingiz noto'g'ri!")
                else:
                    if new_password != confirmed_new_password:
                        return HttpResponse(request, "Yangi parolingiz tasdiqlash paroliga mos kelmaydi!")

                    elif len(new_password) < 5 or  \
                            not any(i.isdigit() for i in new_password):
                        return HttpResponse("Parolingiz juda zaif!")

                    else:
                        user.set_password(new_password)
                        user.save()
                        update_session_auth_hash(request, user)

                        return HttpResponse(request, "Parolingiz muvaffaqiyatli o'zgartirildi!")
                        success_url = 'admin_home_page'
                        return redirect(success_url)

        else:
            return HttpResponse(request, " Kechirasiz, barcha maydonlarni to'ldirish shart!")

    context = {

    }
    return render(request, "admin/reset-password.html", context)



def logout(request):
    auth.logout(request)
    request.session.flush()
    return redirect("auth_login")


def admin_news_list(request):
    news_list = New.object.filter().order_by('-date')[:20]
    categories = Category.objects.all()
    category = SubCategory.objects.all()


    context = {
        'admin_news_list': news_list,
        'admin_categories': categories,
        'admin_sub_categories': category,
    }

    return render(request, 'admin/post/news_list.html', context)


class AdminPostDetailView(DetailView):
    model = New
    template_name = 'admin/post/news_detail.html'
    context_object_name = 'news'


class AdminNewsUpdateView(UpdateView):
    #print('aaa')
    model = New
    form_class = AdminNewsUpdateForm
    # fields = ('name', 'description', 'full_info', 'header_images', 'category', 'sub_category', 'status')
    template_name = 'admin/post/edit/update.html'
    success_url = reverse_lazy('admin_news_list')
