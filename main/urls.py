from django.urls import path, include
from .import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('noticeboard', views.noticeboard, name='noticeboard'),
    path('complaint/', views.complaint, name='complaint'),
    path('staff/', views.staff, name='staff'),
    path('makenotice', views.makenotice, name='makenotice'),
    path('service', views.service, name='service'),
    path('searchbill', views.searchbill, name='searchbill'),
    path('<int:bill_id>/', views.viewbill, name='viewbill'),
    path('addvisitor', views.addvisitor, name='addvisitor'),
    path('visitor', views.visitor, name='visitor'),
    path('test', views.test, name='test'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
