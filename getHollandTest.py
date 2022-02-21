import requests
from pandas import json_normalize
import json
import pandas as pd
from openpyxl.workbook import workbook
import urllib.request
import inspect
import os

Service_Key = '29d8f861a947e7a170ef4184637eba9a'
Test_Type = '&q=18'
url= 'http://www.career.go.kr/inspct/openapi/test/questions?apikey='+ Service_Key + Test_Type
nTotalQuestion = 155

res = requests.get(url)
print(res.text)

data=json.loads(res.text)
jsonArray = data.get("RESULT")
question = []
questionNumber = []
option1 = []
option2 = []

for list in jsonArray:
    question.append(list.get("question"))
    questionNumber.append(list.get("qitemNo"))
    option1.append(list.get("tip1Desc"))
    option2.append(list.get("tip2Desc"))

td = {'문항 번호':questionNumber,'질문':question, '부연1':option1, '부연2':option2}
questionList = pd.DataFrame(td)
# print(questionList)

path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
file_name = path+'\\files\\'+'흥미검사 질문 리스트.xlsx'
questionList.to_excel(excel_writer=file_name)


    

    
    