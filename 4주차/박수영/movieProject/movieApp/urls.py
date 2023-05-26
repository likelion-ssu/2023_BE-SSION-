"""
URL configuration for movieProject project.

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
from django.urls import path
from movieApp import views


urlpatterns = [
    # path('', views.movie_list),
    path('', views.MovieListView.as_view()),
    # path('<int:id>/', views.movie_detail)
    path('<int:id>/', views.MovieDetailView.as_view()),
    path('<int:id>/reviews/', views.MovieReviewListView.as_view()),
    path('<int:id>/reviews/<int:review_id>/', views.MovieReviewDetailView.as_view())
]
