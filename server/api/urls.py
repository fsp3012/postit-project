from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home ),
    path('protected/', views.protected_view ),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('stories/', views.all_stories),
    path('stories/create/', views.create_story),
    path('stories/user/', views.user_stories),
    path('stories/<int:id>/', views.single_story),
]