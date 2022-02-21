# job-info

- 다음의 코드를 포함하면 파일을 실행의 산출물이 파일 실행 위치 내 file 디렉토리에 저장된다.
  
  ```python
  path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
  file_name = path+'\\files\\'+'흥미검사 질문 리스트.xlsx'
  questionList.to_excel(excel_writer=file_name)
  ```

- .ignore 파일에 의해 files 디렉토리 내 파일은 git에 기록되지 않는다.



## getHollandTest.py

매뉴얼에 따르면 tip1Desc와 tip2Desc 컬럼에 문항 이해에 도움이 될만한 부연 정보가 포함되어야 하는데, 실제로 api를 통해 json을 받으면 문항 번호와 질문 내용만 담고 있다. 기술적 장애인지 애초에 자료가 입력이 안 된 것인지 확인하지 못했다.