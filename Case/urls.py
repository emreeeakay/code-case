from django.urls import path
from . import views

urlpatterns = [
    path('save', views.getData),
    path('daily/<day>', views.getDaily),
    path('weekly/<week>', views.getWeekly),
    path('monthly/<month>', views.getMonthly),
    path('yearsly/<years>', views.getYears)
]
