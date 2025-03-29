from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.shortcuts import render, redirect  
from .models import *
from .forms import *
from .serializers import *
from django.urls import reverse
from django.http import HttpResponseNotAllowed
# Create your views here.
from django.apps import apps
from django.forms import modelform_factory

APP_NAME = 'adminpage'

def dynamic_index(request, model_name):
    Model = apps.get_model(APP_NAME, model_name)  # ✅ adminpage 내 모델 가져오기
    objects = Model.objects.all()

    # 필드 목록 가져오기
    fields = [field.verbose_name for field in Model._meta.fields]
    field_names = [field.name for field in Model._meta.fields]

    return render(request, "show.html", {
        'objects': objects,
        'model_name': model_name,
        'fields': fields,
        'field_names': field_names
    })

def dynamic_add(request, model_name):
    Model = apps.get_model(APP_NAME, model_name)
    FormClass = modelform_factory(Model, fields="__all__")

    if request.method == "POST":
        form = FormClass(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("adminpage:dynamic_index", args=[model_name]))
    else:
        form = FormClass()

    return render(request, 'index.html', {'form': form, 'model_name': model_name})

def dynamic_edit(request, model_name, id):
    Model = apps.get_model(APP_NAME, model_name)
    obj = get_object_or_404(Model, pk=id)

    FormClass = modelform_factory(Model, fields="__all__")

    if request.method == "POST":
        form = FormClass(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(reverse("adminpage:dynamic_index", args=[model_name]))
    else:
        form = FormClass(instance=obj)

    return render(request, 'edit.html', {'form': form, 'model_name': model_name, 'obj': obj})

def dynamic_delete(request, model_name, id):
    Model = apps.get_model(APP_NAME, model_name)
    obj = get_object_or_404(Model, pk=id)

    if request.method == "POST":
        obj.delete()
        return redirect(reverse("adminpage:dynamic_index", args=[model_name]))
    else:
        return HttpResponseNotAllowed(["POST"])




# def defaultpage(request):
#     return render(request,'default.html')


# def SCBD1001(request):
#     commoncd = CommonCode.objects.all().values(
#         'com_cd_id', 'cd_sep', 'hr_cd', 'cd_nm', 'cd_exp',
#         'assi_char_prop1', 'assi_char_prop2', 'assi_char_prop3','assi_num_prop1','assi_num_prop2','assi_num_prop3',
#         'note', 'inpu_dt', 'inpu_peo', 'modi_dt', 'modi_peo'
#     )

#     # 날짜 데이터를 문자열(ISO 8601 형식)로 변환
#     commoncd_list = []
#     for item in commoncd:
#         item = dict(item)  # QuerySet을 dict로 변환
#         item['inpu_dt'] = item['inpu_dt'].isoformat() if item['inpu_dt'] else None
#         item['modi_dt'] = item['modi_dt'].isoformat() if item['modi_dt'] else None
#         commoncd_list.append(item)

#     # JSON 직렬화 (한글 깨짐 방지)
#     commoncd_json = json.dumps(commoncd_list, ensure_ascii=False)

#     return render(request, 'SC-BD-1001.html', {'commoncd': commoncd_json})

# @api_view(['GET', 'POST'])
# def SCBD1001api(request):
#     if request.method == 'GET':
#         items = CommonCode.objects.all()
#         serializer = CommonCodeSerializer(items, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = CommonCodeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # 상세 조회, 수정, 삭제
# @api_view(['GET', 'PUT', 'DELETE'])
# def SCBD1001detail(request, pk):
#     item = get_object_or_404(CommonCode, pk=pk)

#     if request.method == 'GET':
#         serializer = CommonCodeSerializer(item)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = CommonCodeSerializer(item, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         item.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# def SCBD1002(request):
#     return render(request,'SC-BD-1002.html')

# def SCBD1003(request):
#     return render(request,'SC-BD-1003.html')

# def SCBD1004(request):
#     return render(request,'SC-BD-1004.html')

# def SCBD2001(request):
#     return render(request,'SC-BD-2001.html')

# # 전체 목록 & 생성
# @api_view(['GET', 'POST'])
# def item_listapi(request):
#     if request.method == 'GET':
#         items = CommonCode.objects.all()
#         serializer = CommonCodeSerializer(items, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = CommonCodeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# # Create your views here.  
# def addnew(request):  
#     if request.method == "POST":  
#         form = CommonCodeForm(request.POST)  
#         if form.is_valid():  
#             try:  
#                 form.save()  
#                 return redirect(reverse("adminpage"))  
#             except:  
#                 pass 
#     else:  
#         form = CommonCodeForm()  
#     return render(request,'index.html',{'form':form})  
# def index(request):  
#     commoncodes = CommonCode.objects.all()  
#     return render(request,"show.html",{'commoncodes':commoncodes})  
# def edit(request, id):  
#     commoncode = CommonCode.objects.get(com_cd_id=id)  
#     return render(request,'edit.html', {'commoncode':commoncode})  
# def update(request, id):  
#     commoncode = CommonCode.objects.get(com_cd_id=id)  
#     form = CommonCodeForm(request.POST, instance = commoncode)  
#     if form.is_valid():  
#         form.save()  
#         return redirect(reverse("adminpage"))  
#     return render(request, 'edit.html', {'commoncode': commoncode})  
# def destroy(request, id):  
#     commoncode = CommonCode.objects.get(com_cd_id=id)  
#     commoncode.delete()  
#     return redirect(reverse("adminpage"))  




# def addnew(request):
#     if request.method == "POST":
#         form = CommonCodeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("adminpage")
#     else:
#         form = CommonCodeForm()
#     return render(request, 'index.html', {'form': form})

# def index(request):
#     commoncodes = CommonCode.objects.all()
#     return render(request, "show.html", {'commoncodes': commoncodes})

# def edit(request, id):
#     commoncode = get_object_or_404(CommonCode, com_cd_id=id)
#     return render(request, 'edit.html', {'commoncode': commoncode})

# def update(request, id):
#     commoncode = get_object_or_404(CommonCode, com_cd_id=id)
    
#     if request.method == "POST":
#         form = CommonCodeForm(request.POST, instance=commoncode)
#         if form.is_valid():
#             form.save()
#             return redirect("adminpage")
#     else:
#         return HttpResponseNotAllowed(["POST"])
    
#     return render(request, 'edit.html', {'commoncode': commoncode})

# def destroy(request, id):
#     if request.method == "POST":
#         commoncode = get_object_or_404(CommonCode, com_cd_id=id)
#         commoncode.delete()
#         return redirect("adminpage")
#     else:
#         return HttpResponseNotAllowed(["POST"])