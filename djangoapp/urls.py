from django.urls import path
from . import views

'''
When somebody requests a page from your website – say, “/knit/34/”, 
Django will load the mysite.urls Python module because it’s pointed to by the ROOT_URLCONF setting.
It finds the variable named urlpatterns and traverses the patterns in order.
After finding the match at 'knit/', it strips off the matching text ("knit/")
and sends the remaining text – "34/" – to the ‘knit.urls’ URLconf for further processing. 
There it matches '<int:product_id>/', resulting in a call to the detail() view like so:
            detail(request=<HttpRequest object>, product_id=34)
'''
urlpatterns = [
    # ex: /knit/
    path('', views.IndexView.as_view(), name='index'),
    path('monitor', views.MonitorView.as_view(), name='monitor'),
    # ex: /knit/12/
    path('<int:pk>/detail/', views.ProductDetailView.as_view(), name='detail'),
    # ex: /knit/12/edit
    path('new_product/', views.ProductAddView.as_view(), name='new_product'),
    path('<int:pk>/edit/', views.ProductUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view(), name='delete'),

]
