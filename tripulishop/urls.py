
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    
]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT);
# handler404='app.views.error404'
# handler500='app.views.error500'
# handler400='app.views.error404'
