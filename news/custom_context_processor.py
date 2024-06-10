from .models import New, Category, SubCategory


def news_list(request):
    news_list = New.published.all().order_by('-date')
    news_list_home = New.published.all().order_by('-date')
    news_list_top = New.published.all().order_by('-date')[:3]
    categories = Category.objects.all()
    category = SubCategory.objects.all()

    context = {
        'news_list': news_list,
        'news_list_home': news_list_home,
        'news_list_top': news_list_top,
        'categories': categories,
        'sub_categories': category,
    }

    return (context)
