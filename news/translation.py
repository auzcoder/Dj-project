from modeltranslation.translator import register, TranslationOptions
from .models import New, Category

@register(New)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'full_info')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)