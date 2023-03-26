from django.urls import path
from accounts.views import user_login, AdminHomePageView, change_password, logout, \
    admin_news_list, AdminNewsUpdateView, AdminPostDetailView

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('home/', AdminHomePageView.as_view(), name='admin_home_page'),
    path('login/', user_login, name='auth_login'),
    path('logout/', logout, name='auth_logout'),
    path('pass-change/', change_password, name='change_password'),
    path('pass-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('pass-reset/', reset_password, name='reset_password')
    path('list/', admin_news_list, name='admin_news_list'),
    path('list/detail/<slug:slug>/', AdminPostDetailView.as_view(), name='admin_news_detail'),
    path('list/edit/<slug:slug>/', AdminNewsUpdateView.as_view(), name='admin_news_update')
]