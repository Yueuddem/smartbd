from django.db import models

#common_code
class CommonCode(models.Model):
    com_cd_id = models.CharField(max_length=9, primary_key=True, verbose_name="공통코드ID")
    cd_sep = models.CharField(max_length=1, blank=True, null=True, verbose_name="코드구분")
    hr_cd = models.CharField(max_length=9, blank=True, null=True, verbose_name="상위코드")
    cd_nm = models.CharField(max_length=100, blank=True, null=True, verbose_name="코드명")
    cd_exp = models.CharField(max_length=4000, blank=True, null=True, verbose_name="코드설명")
    assi_char_prop1 = models.CharField(max_length=200, blank=True, null=True, verbose_name="보조문자속성1")
    assi_char_prop2 = models.CharField(max_length=200, blank=True, null=True, verbose_name="보조문자속성2")
    assi_char_prop3 = models.CharField(max_length=200, blank=True, null=True, verbose_name="보조문자속성3")
    assi_num_prop1 = models.FloatField(blank=True, null=True, verbose_name="보조숫자속성1")
    assi_num_prop2 = models.FloatField(blank=True, null=True, verbose_name="보조숫자속성2")
    assi_num_prop3 = models.FloatField(blank=True, null=True, verbose_name="보조숫자속성3")
    note = models.CharField(max_length=4000, blank=True, null=True, verbose_name="비고")
    inpu_dt = models.DateField(blank=True, null=True, verbose_name="입력일시",auto_now_add=True)
    inpu_peo = models.CharField(max_length=20, blank=True, null=True, verbose_name="입력자")
    modi_dt = models.DateField(blank=True, null=True, verbose_name="수정일시")
    modi_peo = models.CharField(max_length=20, blank=True, null=True, verbose_name="수정자")

    class Meta:
        db_table = 'common_code'
        verbose_name = "공통 코드"
        verbose_name_plural = "공통 코드 목록"

    def __str__(self):
        return self.com_cd_id
    
#customer_collection_info
class CustomerCollectionInfo(models.Model):
    data_gat_dt = models.CharField(max_length=8, verbose_name="자료수집기준일자")
    cust_id = models.CharField(max_length=4, verbose_name="고객사ID")
    tb_id = models.CharField(max_length=10, verbose_name="테이블ID")
    data_num = models.BigIntegerField(verbose_name="자료순번")
    data_gat_sep_cd = models.CharField(max_length=9, blank=True, null=True, verbose_name="자료수집구분코드")
    
    # 데이터 항목 텍스트 컬럼들
    for i in range(1, 91):
        locals()[f"data_cat_txt{i}"] = models.TextField(blank=True, null=True, verbose_name=f"자료항목텍스트{i}")
    
    inpu_dt = models.DateField(blank=True, null=True, verbose_name="입력일시")
    inpu_peo = models.CharField(max_length=20, blank=True, null=True, verbose_name="입력자")
    modi_dt = models.DateField(blank=True, null=True, verbose_name="수정일시")
    modi_peo = models.CharField(max_length=20, blank=True, null=True, verbose_name="수정자")
    
    class Meta:
        db_table = 'customer_collection_info'
        verbose_name = "고객사 데이터 수집 정보"
        verbose_name_plural = "고객사 데이터 수집 정보 목록"
        constraints = [
            models.UniqueConstraint(fields=['data_gat_dt', 'cust_id', 'tb_id', 'data_num'], name='unique_data_gat_dt_cust_id_tb_id_data_num')
        ]
    
    def __str__(self):
        return f"{self.data_gat_dt} - {self.cust_id} - {self.tb_id} - {self.data_num}"


#customer_gather_table_info
class CustomerGatherTableInfo(models.Model):
    cust_id = models.CharField(max_length=4, verbose_name="고객사ID")
    tb_id = models.CharField(max_length=10, verbose_name="테이블ID")
    tb_nm = models.CharField(max_length=10, blank=True, null=True, verbose_name="테이블명")
    tb_exp = models.CharField(max_length=4000, blank=True, null=True, verbose_name="테이블설명")
    info_gat_sc_cd = models.CharField(max_length=20, blank=True, null=True, verbose_name="정보수집출처코드")
    info_gat_typ_cd = models.CharField(max_length=1000, blank=True, null=True, verbose_name="정보수집유형코드")
    info_gat_web = models.CharField(max_length=100, blank=True, null=True, verbose_name="정보수집처웹주소")
    note = models.CharField(max_length=4000, blank=True, null=True, verbose_name="비고")
    inpu_dt = models.DateField(blank=True, null=True, verbose_name="입력일시")
    inpu_peo = models.CharField(max_length=20, blank=True, null=True, verbose_name="입력자")
    modi_dt = models.DateField(blank=True, null=True, verbose_name="수정일시")
    modi_peo = models.CharField(max_length=20, blank=True, null=True, verbose_name="수정자")
    info_typ_cd = models.CharField(max_length=20, blank=True, null=True, verbose_name="정보유형코드")
    
    class Meta:
        db_table = 'customer_gather_table_info'
        verbose_name = "고객사 수집 테이블 정보"
        verbose_name_plural = "고객사 수집 테이블 정보 목록"
        constraints = [
            models.UniqueConstraint(fields=["cust_id", "tb_id"], name='unique_cust_id_tb_id')
        ]
    
    def __str__(self):
        return f"{self.cust_id} - {self.tb_id}"

#customer_info
class CustomerInfo(models.Model):
    cust_id = models.CharField(max_length=4, primary_key=True, verbose_name="고객사ID")
    cust_nm = models.CharField(max_length=100, blank=True, null=True, verbose_name="고객사명")
    cust_info = models.CharField(max_length=4000, blank=True, null=True, verbose_name="고객사정보")
    cust_tel = models.CharField(max_length=20, blank=True, null=True, verbose_name="고객사대표번호")
    cust_addr = models.CharField(max_length=1000, blank=True, null=True, verbose_name="고객사주소")
    mg_nm = models.CharField(max_length=100, blank=True, null=True, verbose_name="담당자명")
    mg_em = models.CharField(max_length=100, blank=True, null=True, verbose_name="담당자이메일")
    mg_tel = models.CharField(max_length=20, blank=True, null=True, verbose_name="담당자연락처")
    note = models.CharField(max_length=4000, blank=True, null=True, verbose_name="비고")
    inpu_dt = models.DateField(blank=True, null=True, verbose_name="입력일시")
    inpu_peo = models.CharField(max_length=20, blank=True, null=True, verbose_name="입력자")
    modi_dt = models.DateField(blank=True, null=True, verbose_name="수정일시")
    modi_peo = models.CharField(max_length=20, blank=True, null=True, verbose_name="수정자")
    
    class Meta:
        db_table = 'customer_info'
        verbose_name = "고객사 정보"
        verbose_name_plural = "고객사 정보 목록"
    
    def __str__(self):
        return self.cust_id
    
#customer_pre_process_history
class CustomerPreProcessHistory(models.Model):
    cust_pre_proc_hist_id = models.CharField(max_length=20, primary_key=True, verbose_name="고객사전처리이력ID")
    cust_id = models.CharField(max_length=4, verbose_name="고객사ID")
    tb_id = models.CharField(max_length=10, verbose_name="테이블ID")
    proc_typ_cd = models.CharField(max_length=10, verbose_name="처리유형코드")
    proc_dt = models.DateField(verbose_name="처리일시")
    result = models.CharField(max_length=9, blank=True, null=True, verbose_name="결과코드")
    note = models.CharField(max_length=4000, blank=True, null=True, verbose_name="비고")
    inpu_dt = models.DateField(blank=True, null=True, verbose_name="입력일시")
    inpu_peo = models.CharField(max_length=20, blank=True, null=True, verbose_name="입력자")
    modi_dy = models.DateField(blank=True, null=True, verbose_name="수정일시")
    modi_peo = models.CharField(max_length=20, blank=True, null=True, verbose_name="수정자")
    
    class Meta:
        db_table = 'customer_pre_process_history'
        verbose_name = "고객사 전처리 이력"
        verbose_name_plural = "고객사 전처리 이력 목록"
    
    def __str__(self):
        return self.cust_pre_proc_hist_id


#customer_pre_process_history
class CustomerPreProcessStandard(models.Model):
    cust_id = models.CharField(max_length=4, db_column='CUST_ID', verbose_name='고객사ID')
    tb_id = models.CharField(max_length=10, db_column='TB_ID', verbose_name='테이블ID')
    col_num = models.BigIntegerField(db_column='COL_NUM', verbose_name='컬럼순번')
    col_typ_cd = models.CharField(max_length=100, null=True, blank=True, db_column='COL_TYP_CD', verbose_name='컬럼유형코드')
    col_all_dg = models.FloatField(null=True, blank=True, db_column='COL_ALL_DG', verbose_name='컬럼총자릿수')
    dp_dg = models.FloatField(null=True, blank=True, db_column='DP_DG', verbose_name='소숫점자릿수')
    note = models.TextField(null=True, blank=True, db_column='NOTE', verbose_name='비고')
    inpu_dt = models.DateField(null=True, blank=True, db_column='INPU_DT', verbose_name='입력일시')
    inpu_peo = models.CharField(max_length=20, null=True, blank=True, db_column='INPU_PEO', verbose_name='입력자')
    modi_dy = models.DateField(null=True, blank=True, db_column='MODI_DY', verbose_name='수정일시')
    modi_peo = models.CharField(max_length=20, null=True, blank=True, db_column='MODI_PEO', verbose_name='수정자')

    class Meta:
        db_table = 'customer_pre_process_standard'
        verbose_name = '고객사 사전 처리 표준'
        verbose_name_plural = '고객사 사전 처리 표준 목록'
        constraints = [
            models.UniqueConstraint(fields=['cust_id', 'tb_id', 'col_num'], name='unique_cust_id_tb_id_col_num')
        ]

    def __str__(self):
        return f'{self.cust_id} - {self.tb_id} - {self.col_num}'