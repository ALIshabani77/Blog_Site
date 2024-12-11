from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("",views.StartingPageView.as_view(),name="starting-page"),
    path("posts",views.AllPostsView.as_view(),name="posts-page"),
    path("posts/<slug:slug>",views.SinglePostView.as_view(),name="post-detail-page"),
    path("read-later",views.ReadLaterView.as_view(),name="read-later"),
     path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
   # path('', views.StartingPageView.as_view(), name='home'),  # صفحه اصلی
]

