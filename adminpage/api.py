from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets, serializers, status
from django.db.models import Q
from .serializers import *
from .models import (
    CommonCode, CustomerCollectionInfo, CustomerGatherTableInfo, 
    CustomerInfo, CustomerPreProcessHistory, CustomerPreProcessStandard
)

# API Views
def handle_request(request, model, serializer_class, lookup_field):
    if request.method == 'GET':
        filters = Q()
        for key in serializer_class.Meta.fields:
            value = request.query_params.get(key, '').strip()
            if value:
                if ',' in value:  # 여러 개의 값이 전달된 경우
                    filters &= Q(**{f"{key}__in": value.split(',')})
                else:
                    filters &= Q(**{f"{key}__exact": value})
        queryset = model.objects.filter(filters)
        serializer = serializer_class(queryset, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
    elif request.method == 'POST':
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        instance = model.objects.get(**{lookup_field: request.data.get(lookup_field)})
        serializer = serializer_class(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        instance = model.objects.get(**{lookup_field: request.query_params.get(lookup_field)})
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def common_code_api(request):
    com_cd_id = request.query_params.get('com_cd_id')
    cd_sep = request.query_params.get('cd_sep')
    hr_cd = request.query_params.get('hr_cd')
    cd_nm = request.query_params.get('cd_nm')
    cd_exp = request.query_params.get('cd_exp')
    assi_char_prop1 = request.query_params.get('assi_char_prop1')
    assi_char_prop2 = request.query_params.get('assi_char_prop2')
    assi_char_prop3 = request.query_params.get('assi_char_prop3')
    assi_num_prop1 = request.query_params.get('assi_num_prop1')
    assi_num_prop2 = request.query_params.get('assi_num_prop2')
    assi_num_prop3 = request.query_params.get('assi_num_prop3')
    note = request.query_params.get('note')
    inpu_dt = request.query_params.get('inpu_dt')
    inpu_peo = request.query_params.get('inpu_peo')
    modi_dt = request.query_params.get('modi_dt')
    modi_peo = request.query_params.get('modi_peo')
    
    queryset = CommonCode.objects.all()
    
    if com_cd_id:
        queryset = queryset.filter(com_cd_id=com_cd_id)
    if cd_sep:
        queryset = queryset.filter(cd_sep=cd_sep)
    if hr_cd:
        queryset = queryset.filter(hr_cd=hr_cd)
    if cd_nm:
        queryset = queryset.filter(cd_nm=cd_nm)
    if cd_exp:
        queryset = queryset.filter(cd_exp=cd_exp)
    if assi_char_prop1:
        queryset = queryset.filter(assi_char_prop1=assi_char_prop1)
    if assi_char_prop2:
        queryset = queryset.filter(assi_char_prop2=assi_char_prop2)
    if assi_char_prop3:
        queryset = queryset.filter(assi_char_prop3=assi_char_prop3)
    if assi_num_prop1:
        queryset = queryset.filter(assi_num_prop1=assi_num_prop1)
    if assi_num_prop2:
        queryset = queryset.filter(assi_num_prop2=assi_num_prop2)
    if assi_num_prop3:
        queryset = queryset.filter(assi_num_prop3=assi_num_prop3)
    if note:
        queryset = queryset.filter(note=note)
    if inpu_dt:
        queryset = queryset.filter(inpu_dt=inpu_dt)
    if inpu_peo:
        queryset = queryset.filter(inpu_peo=inpu_peo)
    if modi_dt:
        queryset = queryset.filter(modi_dt=modi_dt)
    if modi_peo:
        queryset = queryset.filter(modi_peo=modi_peo)


    serializer = CommonCodeSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def customer_collection_info_api(request):
    data_gat_dt = request.query_params.get('data_gat_dt')
    cust_id = request.query_params.get('cust_id')
    tb_id = request.query_params.get('tb_id')
    data_num = request.query_params.get('data_num')
    data_gat_sep_cd = request.query_params.get('data_gat_sep_cd')
    inpu_dt = request.query_params.get('inpu_dt')
    inpu_peo = request.query_params.get('inpu_peo')
    modi_dt = request.query_params.get('modi_dt')
    modi_peo = request.query_params.get('modi_peo')

    queryset = CustomerCollectionInfo.objects.all()
    
    if data_gat_dt:
        queryset = queryset.filter(data_gat_dt=data_gat_dt)
    if cust_id:
        queryset = queryset.filter(cust_id=cust_id)
    if tb_id:
        queryset = queryset.filter(tb_id=tb_id)
    if data_num:
        queryset = queryset.filter(data_num=data_num)
    if data_gat_sep_cd:
        queryset = queryset.filter(data_gat_sep_cd=data_gat_sep_cd)
    if inpu_dt:
        queryset = queryset.filter(inpu_dt=inpu_dt)
    if inpu_peo:
        queryset = queryset.filter(inpu_peo=inpu_peo)
    if modi_dt:
        queryset = queryset.filter(modi_dt=modi_dt)
    if modi_peo:
        queryset = queryset.filter(modi_peo=modi_peo)


    serializer = CustomerCollectionInfoSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def customer_gather_table_info_api(request):
    cust_id = request.query_params.get('cust_id')
    tb_id = request.query_params.get('tb_id')
    tb_nm = request.query_params.get('tb_nm')
    tb_exp = request.query_params.get('tb_exp')
    info_gat_sc_cd = request.query_params.get('info_gat_sc_cd')
    info_gat_typ_cd = request.query_params.get('info_gat_typ_cd')
    info_gat_web = request.query_params.get('info_gat_web')
    note = request.query_params.get('note')
    inpu_dt = request.query_params.get('inpu_dt')
    inpu_peo = request.query_params.get('inpu_peo')
    modi_dt = request.query_params.get('modi_dt')
    modi_peo = request.query_params.get('modi_peo')
    modi_peo = request.query_params.get('modi_peo')
    info_typ_cd = request.query_params.get('info_typ_cd')

    queryset = CustomerGatherTableInfo.objects.all()
    
    if cust_id:
        queryset = queryset.filter(cust_id=cust_id)
    if tb_id:
        queryset = queryset.filter(tb_id=tb_id)
    if tb_nm:
        queryset = queryset.filter(tb_nm=tb_nm)
    if tb_exp:
        queryset = queryset.filter(tb_exp=tb_exp)
    if info_gat_sc_cd:
        queryset = queryset.filter(info_gat_sc_cd=info_gat_sc_cd)
    if info_gat_typ_cd:
        queryset = queryset.filter(info_gat_typ_cd=info_gat_typ_cd)
    if info_gat_web:
        queryset = queryset.filter(info_gat_web=info_gat_web)
    if note:
        queryset = queryset.filter(note=note)
    if inpu_dt:
        queryset = queryset.filter(inpu_dt=inpu_dt)
    if inpu_peo:
        queryset = queryset.filter(inpu_peo=inpu_peo)
    if modi_dt:
        queryset = queryset.filter(modi_dt=modi_dt)
    if modi_peo:
        queryset = queryset.filter(modi_peo=modi_peo)
    if info_typ_cd:
        queryset = queryset.filter(info_typ_cd=info_typ_cd)


    serializer = CustomerGatherTableInfoSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def customer_info_api(request):
    cust_id = request.query_params.get('cust_id')
    cust_nm = request.query_params.get('cust_nm')
    cust_info = request.query_params.get('cust_info')
    cust_tel = request.query_params.get('cust_tel')
    cust_addr = request.query_params.get('cust_addr')
    mg_nm = request.query_params.get('mg_nm')
    mg_em = request.query_params.get('mg_em')
    mg_tel = request.query_params.get('mg_tel')
    note = request.query_params.get('note')
    inpu_dt = request.query_params.get('inpu_dt')
    inpu_peo = request.query_params.get('inpu_peo')
    modi_dt = request.query_params.get('modi_dt')
    modi_peo = request.query_params.get('modi_peo')

    queryset = CustomerInfo.objects.all()
    
    if cust_id:
        queryset = queryset.filter(cust_id=cust_id)
    if cust_nm:
        queryset = queryset.filter(cust_nm=cust_nm)
    if cust_info:
        queryset = queryset.filter(cust_info=cust_info)
    if cust_tel:
        queryset = queryset.filter(cust_tel=cust_tel)
    if cust_addr:
        queryset = queryset.filter(cust_addr=cust_addr)
    if mg_nm:
        queryset = queryset.filter(mg_nm=mg_nm)
    if mg_em:
        queryset = queryset.filter(mg_em=mg_em)
    if mg_tel:
        queryset = queryset.filter(mg_tel=mg_tel)
    if note:
        queryset = queryset.filter(note=note)
    if inpu_dt:
        queryset = queryset.filter(inpu_dt=inpu_dt)
    if inpu_peo:
        queryset = queryset.filter(inpu_peo=inpu_peo)
    if modi_dt:
        queryset = queryset.filter(modi_dt=modi_dt)
    if modi_peo:
        queryset = queryset.filter(modi_peo=modi_peo)

    serializer = CustomerInfoSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False,json_dumps_params={'ensure_ascii': False})
    
@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def customer_pre_process_history_api(request):
    cust_id = request.query_params.get('cust_id')
    cust_pre_proc_hist_id = request.query_params.get('cust_pre_proc_hist_id')
    tb_id = request.query_params.get('tb_id')
    proc_typ_cd = request.query_params.get('proc_typ_cd')
    proc_dt = request.query_params.get('proc_dt')
    result = request.query_params.get('result')
    note = request.query_params.get('note')
    inpu_dt = request.query_params.get('inpu_dt')
    inpu_peo = request.query_params.get('inpu_peo')
    modi_dy = request.query_params.get('modi_dy')
    modi_peo = request.query_params.get('modi_peo')

    queryset = CustomerInfo.objects.all()
    
    if cust_id:
        queryset = queryset.filter(cust_id=cust_id)
    if cust_pre_proc_hist_id:
        queryset = queryset.filter(cust_pre_proc_hist_id=cust_pre_proc_hist_id)
    if tb_id:
        queryset = queryset.filter(tb_id=tb_id)
    if proc_typ_cd:
        queryset = queryset.filter(proc_typ_cd=proc_typ_cd)
    if proc_dt:
        queryset = queryset.filter(proc_dt=proc_dt)
    if result:
        queryset = queryset.filter(result=result)
    if note:
        queryset = queryset.filter(note=note)
    if inpu_dt:
        queryset = queryset.filter(inpu_dt=inpu_dt)
    if inpu_peo:
        queryset = queryset.filter(inpu_peo=inpu_peo)
    if modi_dy:
        queryset = queryset.filter(modi_dy=modi_dy)
    if modi_peo:
        queryset = queryset.filter(modi_peo=modi_peo)

    serializer = CustomerInfoSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
    
@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def customer_pre_process_standard_api(request):
    cust_id = request.query_params.get('cust_id')
    tb_id = request.query_params.get('tb_id')
    col_num = request.query_params.get('col_num')
    col_typ_cd = request.query_params.get('col_typ_cd')
    col_all_dg = request.query_params.get('col_all_dg')
    dp_dg = request.query_params.get('dp_dg')
    note = request.query_params.get('note')
    inpu_dt = request.query_params.get('inpu_dt')
    inpu_peo = request.query_params.get('inpu_peo')
    modi_dy = request.query_params.get('modi_dy')
    modi_peo = request.query_params.get('modi_peo')

    queryset = CustomerInfo.objects.all()
    
    if cust_id:
        queryset = queryset.filter(cust_id=cust_id)
    if tb_id:
        queryset = queryset.filter(tb_id=tb_id)
    if col_num:
        queryset = queryset.filter(col_num=col_num)
    if col_typ_cd:
        queryset = queryset.filter(col_typ_cd=col_typ_cd)
    if col_all_dg:
        queryset = queryset.filter(col_all_dg=col_all_dg)
    if dp_dg:
        queryset = queryset.filter(dp_dg=dp_dg)
    if note:
        queryset = queryset.filter(note=note)
    if inpu_dt:
        queryset = queryset.filter(inpu_dt=inpu_dt)
    if inpu_peo:
        queryset = queryset.filter(inpu_peo=inpu_peo)
    if modi_dy:
        queryset = queryset.filter(modi_dy=modi_dy)
    if modi_peo:
        queryset = queryset.filter(modi_peo=modi_peo)

    serializer = CustomerInfoSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def customer_collection_info_api_all(request):    
    return handle_request(request, CustomerCollectionInfo, CustomerCollectionInfoSerializer, 'data_gat_dt')

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def customer_gather_table_info_api_all(request):
    return handle_request(request, CustomerGatherTableInfo, CustomerGatherTableInfoSerializer, 'tb_id')

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def customer_info_api_all(request):
    return handle_request(request, CustomerInfo, CustomerInfoSerializer, 'cust_id')

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def customer_pre_process_history_api_all(request):
    return handle_request(request, CustomerPreProcessHistory, CustomerPreProcessHistorySerializer, 'cust_pre_proc_hist_id')

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def customer_pre_process_standard_api_all(request):
    return handle_request(request, CustomerPreProcessStandard, CustomerPreProcessStandardSerializer, 'cust_id')
