from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemap import StaticViewSitemap,BlogSitemap,ProductSitemap,ProductClassSitemap

sitemaps = {
    # 'static': StaticViewSitemap,
    'blog':BlogSitemap,
    'product':ProductSitemap,
    'productclass':ProductClassSitemap
}
urlpatterns = [
    path('', views.index, name='index'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    path('blog', views.blog, name='blog'),
    path('blog/<str:slug>', views.post, name='post'),
    path('product/<str:slug>', views.product_class, name='product_class'),
    path('product/<str:class_slug>/<str:slug>', views.product, name='product'),

]