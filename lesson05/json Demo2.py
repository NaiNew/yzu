import json
import requests

#url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'  # 不合格
url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceQualified.aspx'  # 合格
r = requests.get(url)
# print(r.status_code)
# print(r.text)
bad_rices = json.loads(r.text)
for bad in bad_rices:
    if '新生' in bad.get ('品名'):
        print(bad.get('品名'), bad.get('不合格原因'))

