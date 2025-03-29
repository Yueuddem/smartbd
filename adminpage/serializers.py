from rest_framework import serializers
from .models import (
    CommonCode, CustomerCollectionInfo, CustomerGatherTableInfo, 
    CustomerInfo, CustomerPreProcessHistory, CustomerPreProcessStandard
)

class CommonCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonCode
        fields = '__all__'

class CustomerCollectionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCollectionInfo
        fields = '__all__'

class CustomerGatherTableInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerGatherTableInfo
        fields = '__all__'

class CustomerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInfo
        fields = '__all__'

class CustomerPreProcessHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPreProcessHistory
        fields = '__all__'

class CustomerPreProcessStandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPreProcessStandard
        fields = '__all__'
