''' from django.urls import path,include
from . import views

urlpatterns = [
    path('<int:id>/',views.airport_detail,name='employee_detail')
] '''