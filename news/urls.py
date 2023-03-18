from django.urls import path, include
from .views import PostListView, PostDetailView, NewsUpdateView, NewsDeleteView, NewsSearchView, CategoryListView, \
    CategoryDetailView

# urls
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('edit/<slug:slug>/', NewsUpdateView.as_view(), name='post_edit'),
    path('delete/<slug:slug>/', NewsDeleteView.as_view(), name='post_delete'),
    # path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]