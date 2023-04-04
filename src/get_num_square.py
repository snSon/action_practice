# src/get_num_square.py

import os

# get the input and convert it to int
num = os.environ.get("INPUT_NUM") #action.yml 파일의 변수를 불러옴
if num:
  try:
    num = int(num)
  except Exception:
    exit('ERROR: the INPUT_NUM provided ("{}") is not an integer'.format(num))
    
else:
  num = 1

# to set output, print to shell in following syntax
print(f"::set-output name=num_squared::{num ** 2}") #::set-output name은 함수 실행 후 나온 값을 action.yml 파일로 넘기기 위한 형식
