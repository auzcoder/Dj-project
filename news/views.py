from django.db.models import Q
from django.http import request, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import context
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from hitcount.views import HitCountDetailView

from .models import New, Category
from django.views.generic import TemplateView
from .forms import ContactForm

def HomePageView(request):

    # categories = Category.objects.all()
    news_list = New.published.all().order_by('-date')[6:10] # [:9] bu listdan kelayotgan xabarlar sonini cheklash uchun hozir bu yerdan jami bo'lib 9 dona yangilik keladi
    news_list_home = New.published.all().order_by('-date')[:6]

    context = {
        'news_list': news_list,
        "news_list_home": news_list_home,
    }
    return render(request, 'home.html', context)


# Contact page uchun views
class ContactPageView(TemplateView):
    template_name = 'contact.html'
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }

        return render(request, 'contact.html', context)
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Bog'langaniz uchun tasahkkur!")

        context = {
            'form': form
        }

        return render(request, 'contact.html', context)


# Create your views here. Post listlar uchun
class PostListView(ListView):
    queryset = New.object.filter(status='PB', )
    template_name = 'news/news.html'
    context_object_name = 'news'


# Post detail uchun views
class PostDetailView(HitCountDetailView):
    model = New
    template_name = 'news/news_detail.html'
    context_object_name = 'news'
    count_hit = True


# Category uchun views
class CategoryListView(ListView):
    model = Category
    template_name = 'news/news_detail.html'
    context_object_name = 'category'


class NewsUpdateView(UpdateView):
    model = New
    fields = ('name', 'description', 'full_info', 'header_images', 'category', 'sub_category', 'status')
    template_name = 'news/edit/update.html'
    success_url = reverse_lazy('home')


class NewsDeleteView(DeleteView):
    model = New
    template_name = 'news/edit/delete.html'
    success_url = reverse_lazy('home')


class NewsCreateView(CreateView):
    model = New
    fields = ('name', 'description', 'full_info', 'header_images', 'category', 'sub_category', 'status')
    template_name = 'news/edit/create.html'
    success_url = reverse_lazy('post_list')


class NewsSearchView(ListView):
    model = New
    template_name = 'news/search.html'
    context_object_name = 'all_news'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return New.object.filter(
            Q(name__icontains=query) | Q(full_info__icontains=query)
        )
    