from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('logout', views.logout_view, name='logout2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add_group/', views.AddGroupDonation.as_view(), name='add_group')
]
