from django.urls import path
from main.views import ListPageView, DetailPageView, add_comment_page
from django.views.generic import TemplateView

urlpatterns = [
    path('',ListPageView.as_view(),name='home' ),
    path('page/<slug:slug>/',DetailPageView.as_view(), name='content'),
    path('page/<slug:slug>/add_post/', add_comment_page, name='add_comment'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about')

]