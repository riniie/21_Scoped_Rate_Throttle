from django.contrib import admin
from django.urls import path, include
from api.views import (
    StudentList,
    StudentCreate,
    StudentRetrieve,
    StudentUpdate,
    StudentDestroy
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest/', include('rest_framework.urls')),
    path('student/', StudentList.as_view(), name='student-list'),
    # path('student/', StudentCreate.as_view(), name='student-create'),
    # path('student/<int:pk>/', StudentRetrieve.as_view(), name='student-retrieve'),
    # path('student/<int:pk>/', StudentUpdate.as_view(), name='student-update'),
    # path('student/<int:pk>/', StudentDestroy.as_view(), name='student-destroy'),
]
