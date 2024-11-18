from django.urls import path
from app import views

app_name='app'
urlpatterns = [
   
   path("post/<int:post_id>",views.detail,name="datail"),
   
   path('register/', views.register, name='register'),
   path('login/', views.login_view, name='login'),
   path('', views.home_view, name='home'),
   path('book_collection/', views.book_collection_view, name='book_collection'),

    # Waste management statistics route
    path('statistics/', views.statistics_view, name='statistics'),

    # Profile settings route
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.custom_logout, name='logout'),

    path('home/', views.home_view_l, name='log'),
]