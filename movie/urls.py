from django.urls import path

from movie import views

urlpatterns = [
   path('', views.home, name='doma' ),
   path('home/', views.home, name="home"),
   path('<int:movie_id>', views.detail, name='detail'),
   path('<int:movie_id>/create',  views.createreview, name='createreview'),
   path('review/<int:review_id>', views.updatereview, name='updatereview'),
   path('review/<int:review_id>/delete', views.deletereview, name='deletereview'),
   path('udate/<int:movie_id>',   views.updatemovie, name='updatemovie'),
]