# forms.py
from django import forms
from .models import *

class CommonCodeForm(forms.ModelForm):
    class Meta:
        model = CommonCode
        fields = [ 'com_cd_id', 'cd_sep', 'hr_cd', 'cd_nm', 'cd_exp',
        'assi_char_prop1', 'assi_char_prop2', 'assi_char_prop3','assi_num_prop1',
        'assi_num_prop2','assi_num_prop3','note']

class CustomerCollectionInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerCollectionInfo
        fields = ['data_gat_dt','cust_id', 'tb_id','data_num','data_gat_sep_cd']

class CustomerGatherTableInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerGatherTableInfo
        fields = ['cust_id', 'tb_id','tb_nm','tb_exp',
                  'info_gat_sc_cd','info_gat_typ_cd','info_gat_web','note',]

class CustomerInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = ['cust_id', 'cust_nm','cust_info','cust_tel','cust_addr','mg_nm','mg_em',
                  'mg_tel', 'note']
        
        
        
        
        
    #     widgets = { 'com_cd_id': forms.TextInput(attrs={ 'class': 'form-control' }), 
    #         'cd_sep': forms.TextInput(attrs={ 'class': 'form-control' }),
    #         'hr_cd': forms.TextInput(attrs={ 'class': 'form-control' }),
    #         'cd_nm': forms.TextInput(attrs={ 'class': 'form-control' }),
    #         'cd_exp': forms.TextInput(attrs={ 'class': 'form-control' }),
    #         'assi_char_prop1': forms.TextInput(attrs={ 'class': 'form-control' }),
    #         'assi_char_prop2': forms.TextInput(attrs={ 'class': 'form-control' }),
    #         'assi_char_prop3': forms.TextInput(attrs={ 'class': 'form-control' }),
    #         'assi_num_prop1': forms.NumberInput(attrs={ 'class': 'form-control' }),
    #         'assi_num_prop2': forms.NumberInput(attrs={ 'class': 'form-control' }),
    #         'assi_num_prop3': forms.NumberInput(attrs={ 'class': 'form-control' }),
    #         'note': forms.TextInput(attrs={ 'class': 'form-control' }),
    #   }
