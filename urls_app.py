from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("challenges_app", include("challenges_app.urls"))
]
