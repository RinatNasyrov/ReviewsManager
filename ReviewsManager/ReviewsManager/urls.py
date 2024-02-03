"""
URL configuration for ReviewsManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ReviewsApp import views
from ReviewsApp.views import ReviewAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ReviewsList.as_view()),
    path('list/', views.ReviewsList.as_view(), name='list'),
    path('review/', views.ReviewCreate.as_view(), name='review'),
    path('api/v1/list', ReviewAPIView.as_view({'get':'list'}), name='api_list'),
    path('api/v1/review', ReviewAPIView.as_view({'post': 'create'}), name='api_review'),
]
