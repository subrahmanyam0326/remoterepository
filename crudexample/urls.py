from django.contrib import admin  
from django.urls import path  
from employee import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('emp', views.emp),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
    path('',views.emp)
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)