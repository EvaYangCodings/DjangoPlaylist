from django.urls import path
from zing_it import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('playlist/<int:id>', views.playlist, name="playlist"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)