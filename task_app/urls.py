from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('logout', views.logout_view, name='logout2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add_group/', views.AddGroupDonation.as_view(), name='add_group'),
    path('about/<int:pk>/', views.about.as_view(), name='about'),
    path('change/<int:pk>/', views.UpdateGroupDonation.as_view(), name='change'),
    path('delete1/<int:id>/', views.delete1, name='delete1'),
    path('profile', views.profile, name='profile'),
    path('add_amount/<int:pk>/', views.add_amount, name='add_amount')
]
