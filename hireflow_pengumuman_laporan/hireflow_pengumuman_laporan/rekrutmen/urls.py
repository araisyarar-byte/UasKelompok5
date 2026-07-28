from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

admin.site.site_header = 'HireFlow Administration'
admin.site.site_title = 'HireFlow Admin'
admin.site.index_title = 'Pengelolaan Pengumuman dan Laporan'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('pengumuman_laporan.urls')),
]
