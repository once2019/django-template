from django.contrib import sitemaps
from django.urls import reverse
from .models import Product,ProductClass,Post

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['contact', 'about', 'index']

    def location(self, item):
        return reverse(item)

class BlogSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.modify_time

class ProductSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.modify_time

class ProductClassSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ProductClass.objects.all()
