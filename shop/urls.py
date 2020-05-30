from django.urls import path


from shop import views


app_name = 'shop'


urlpatterns = [
    path('accounts/profile/register', views.UserCreateView.as_view(), name='profile_register'),
    path('accounts/profile/change/<int:pk>/', views.UserUpdateView.as_view(), name='profile_change'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/logout/', views.UserLogoutView.as_view(), name='logout'),
    path('<str:page>/', views.other_page, name='other_page'),
    path('', views.index, name='index')
]
