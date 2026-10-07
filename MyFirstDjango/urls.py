from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from todo_list import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_views.home, name='home'),
    path('about/', todo_views.about, name='about'),
    path('delete/<int:list_id>/', todo_views.delete, name='delete'),
    path('strike/<int:list_id>/', todo_views.strike, name='strike'),
    path('unstrike/<int:list_id>/', todo_views.unstrike, name='unstrike'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
