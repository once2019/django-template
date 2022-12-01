from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.
class ProductClass(models.Model):
    name = models.CharField('产品分类',max_length=255,db_index=True,unique=True)
    slug = models.CharField('url',max_length=255,db_index=True,unique=True)
    img = models.ImageField(upload_to='uploads/imgs/%Y/%m/%d/',verbose_name="产品分类图")

    def get_absolute_url(self):
        return reverse('product_class', kwargs={'slug' : self.slug})
class Product(models.Model):
    name = models.CharField('产品名称',max_length=255,db_index=True,unique=True)
    slug = models.CharField('url',max_length=255,db_index=True,unique=True)
    produc_class = models.ForeignKey(ProductClass,on_delete=models.CASCADE,verbose_name="产品分类",related_name="products")
    img1 = models.ImageField(upload_to='uploads/imgs/%Y/%m/%d/',verbose_name="产品展示图1")
    img2 = models.ImageField(upload_to='uploads/imgs/%Y/%m/%d/',verbose_name="产品展示图2")
    img3 = models.ImageField(upload_to='uploads/imgs/%Y/%m/%d/',verbose_name="产品展示图3")
    img4 = models.ImageField(upload_to='uploads/imgs/%Y/%m/%d/',verbose_name="产品展示图4")
    params = RichTextField('产品参数')
    description = RichTextField('产品描述')
    advantage = RichTextField('产品优势')
    feature = RichTextField('产品特色')
    content = RichTextField('产品介绍')
    file = models.FileField(upload_to='uploads/files/%Y/%m/%d/',verbose_name="产品文档")
    add_time = models.DateTimeField('添加时间',auto_now_add=True)
    modify_time = models.DateTimeField('更新时间',auto_now=True)
    is_actived = models.BooleanField('是否展示',default=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('product', kwargs={'slug' : self.slug, 'class_slug' : self.produc_class.slug })
class Category(models.Model):
    category = models.CharField('类别名称',max_length=255,db_index=True,unique=True)
    def __str__(self):
        return self.category

    class Meta:
        verbose_name:'日志分类'

class Post(models.Model):
    title = models.CharField('标题',max_length=255,db_index=True,unique=True)
    slug = models.CharField('url',max_length=255,db_index=True,unique=True)
    author = models.CharField('作者',max_length=255)
    img = models.ImageField(upload_to='uploads/imgs/%Y/%m/%d/',verbose_name="日志展示图")
    description = RichTextField('概要',)
    content = RichTextField('内容',)
    tag = TaggableManager(blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="分类", related_name="posts")
    pub_time = models.DateTimeField('发布时间',)
    add_time = models.DateTimeField('添加时间',auto_now_add=True)
    modify_time = models.DateTimeField('修改时间',auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug' : self.slug})