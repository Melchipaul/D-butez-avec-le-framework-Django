"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('about-us/', views.about, name='about-us'),
    path('listings/', views.listings, name='listing-list'),
    path('listings/<int:id>/', views.listing_detail, name='listing-detail'),
    path('listings/add/', views.create_new_listing, name='create-listing'),
    path('listings/<int:id>/change/', views.listing_update, name='listing-update'),
    path('listings/<int:id>/delete/', views.listing_delete, name='listing-delete'),
    path('contact-us/', views.nous_contacter, name='contact'),
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    path('bands/<int:id>/change/', views.band_update, name='band-update'),
    path('band_listings/<int:id>/', views.band_listings, name='band-listings'),
    path('bands/add/', views.band_create, name='band-create'),
    path('bands/<int:id>/delete/', views.band_delete, name='band-delete'),
    path('email-sent/', views.email_sent, name='email-sent'),
]

# Servir les fichiers statiques en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
