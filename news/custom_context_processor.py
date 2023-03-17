from .models import New, Category, SubCategory

def news_list(request):
    news_list = New.published.all().order_by('-date')[:5]
    news_list_home = New.published.all().order_by('-date')
    categories = Category.objects.all()
    category = SubCategory.objects.all()

    context = {
        'news_list': news_list,
        'news_list_home': news_list_home,
        'categories': categories,
        'sub_categories': category,
    }

    return (context)