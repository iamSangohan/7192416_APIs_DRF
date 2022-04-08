from rest_framework.viewsets import ReadOnlyModelViewSet

from shop.models import Article, Category, Product
from shop.serializers import ArticleSerializer, CategoryListSerializer, CategoryDetailSerializer, ProductListSerializer, ProductDetailSerializer


class CategoryViewset(ReadOnlyModelViewSet):
    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer
    
    def get_queryset(self):
        return Category.objects.filter(active=True)
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
    
    # @transaction.atomic
    # @action(detail=True, methods=['post'])
    # def disable(self, request, pk):
    #     category = self.get_object()
    #     category.active = False
    #     category.save()
    #     category.products.update(actice=False)
    #     return response()
    

class ProductViewset(ReadOnlyModelViewSet):
    serializer_class = ProductListSerializer
    detail_serializer_class = ProductDetailSerializer
    
    def get_queryset(self):
        queryset = Product.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category_id = category_id)
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ArticleViewset(ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer
    
    def get_queryset(self):
        queryset = Article.objects.filter(active=True)
        product_id = self.request.GET.get('product_id')
        if product_id is not None:
            queryset = queryset.filter(product_id = product_id)
        return queryset