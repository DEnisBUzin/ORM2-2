from django.template.defaulttags import url
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from school.views import students_list
import debug_toolbar

urlpatterns = [
    path('', students_list, name='students'),
    path('admin/', admin.site.urls),
    path(r'__debug__/', include(debug_toolbar.urls)),
]

# if settings.DEBUG:
#
#     urlpatterns = [
#
#     ]