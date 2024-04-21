from django.contrib import admin
from django.urls import path
from startappOne import views as l
from startappTwo import views as t
from startappthree import views as s

urlpatterns = [
    path('admin/', admin.site.urls),
    path('d1/', l.d1),  # http://127.0.0.1:8000/d1/
    path('d2/', t.d2),  # http://127.0.0.1:8000/d2/
    path('d3/', s.d3)   # http://127.0.0.1:8000/d3/
]
