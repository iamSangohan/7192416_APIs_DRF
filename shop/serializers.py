from pyexpat import model
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from shop.models import Article, Category, Product



class CategoryListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name']        


class CategoryDetailSerializer(serializers.ModelSerializer):
    
    products = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'products']
    
    def get_products(self, instance):
        queryset = instance.products.filter(active=True)
        serializer = ProductListSerializer(queryset, many=True)
        return serializer.data


class ProductListSerializer(ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name']
  
        
class ProductDetailSerializer(ModelSerializer):
    
    articles = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'articles']
    
    def get_articles(self, instance):
        queryset = instance.articles.filter(active=True)
        serializer = ArticleSerializer(queryset, many=True)
        return serializer.data

class ArticleSerializer(ModelSerializer):
    
    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 'price', 'product']