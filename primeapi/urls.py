from django.contrib import admin
from django.urls import path
from ladder.views import PrimeView

urlpatterns = [
    path('admin/', admin.site.urls),
    # add the prime endpoint:
    path('api/prime/<int:n>/', PrimeView.as_view(), name='prime'),
]
