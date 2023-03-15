from .models import New, Category, SubCategory

def news_list(request):
    news_list = New.published.all().order_by('-date')[:5]
    categories = Category.objects.all()
    category = SubCategory.objects.all()

    context = {
        'news_list': news_list,
        'categories': categories,
        'sub_categories': category,
    }

    return (context)