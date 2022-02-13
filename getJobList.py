import requests
import json
from pandas import json_normalize
import pandas as pd
from openpyxl.workbook import workbook
import urllib.parse
import urllib.request
import math
import inspect
import os

abilities = ['신체운동능력','손재능','공간지각력','음악능력','창의력','언어능력','수리논리력', '자기성찰능력', '대인관계능력','자연친화력','예술시각능력']
firstAbilityCode = 100829
Service_Key = 'f7ca462bda9a5d6e0fb4bade96407888'
params = '&svcCode=JOB&contentType=Json&gubun=job_apti_list&svcType=api&pgubn='
url_temp = 'http://www.career.go.kr/cnet/openapi/getOpenApi.json?apiKey='+ Service_Key 


for i in range(0, len(abilities)):
    ability_code = firstAbilityCode + i
    specified_params = params + str(ability_code)
    url = url_temp + specified_params +"&perPage=1"
    
    res = requests.get(url)
    # print(res.text)

    data=json.loads(res.text)
    body = data['dataSearch']['content']
    df = json_normalize(body)
    nTotal = df["totalCount"][0]
    nPage = math.ceil(int(nTotal) / 20)

    for page in range(0,nPage):
        pageParam = '&thisPage=' + str(page+1)+"&perPage=20"
        urlInPage = url_temp + specified_params + pageParam
        res = requests.get(urlInPage)
        data=json.loads(res.text)
        body = data['dataSearch']['content']
        dfNew = json_normalize(body)
        df =pd.concat([df,dfNew], ignore_index=False)

    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    current_ability = abilities[i]
    file_name = path+'\\'+current_ability+' 직업 리스트.xlsx'
    print(file_name)
    # df.to_excel(excel_writer=file_name)


    

    
    