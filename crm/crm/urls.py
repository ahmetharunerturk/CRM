from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static


from core.views import index,about
from userprofile.views import signup, myaccount

urlpatterns = [
    path('admin/', admin.site.urls),
    path("dashboard/leads/", include('lead.urls')),
    path("dashboard/clients/", include('client.urls')),
    path("dashboard/teams/", include('team.urls')),
    path("dashboard/", include('dashboard.urls')),
    path("dashboard/myaccount", myaccount, name="myaccount"),
    path('', index, name='index'),
    path('sign-up', signup, name='signup'),
    path("log-in/", views.LoginView.as_view(template_name='userprofile/login.html'), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path('about/', about, name='about'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



