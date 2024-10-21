from django.urls import path
from .views import MyObjectView

urlpatterns = [
    path('api/myobject/', MyObjectView.as_view(), name='myobject'),
]