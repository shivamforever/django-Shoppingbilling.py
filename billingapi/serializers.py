from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class BillSerializer(serializers.ModelSerializer):
    total_amount = serializers.CharField(read_only=True)
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    products = ProductSerializer(many=True)

    class Meta:
        model = Bill
        fields = ['id', 'customer', 'customer_name', 'products', 'total_amount', 'timestamp']
