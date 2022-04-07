from dataclasses import field, fields
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from shop.models import Article, Category, Product


class CategorySerializer(ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'name']
        
        
class ProductsSerializer(ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated','name']
        

class ArticleSerializer(ModelSerializer):
    
    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 'price', 'product']