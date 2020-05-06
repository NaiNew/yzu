import json

score = '{"國文":100, "數學":80}'
students = '[{"name":"Edward", "age":27},{"name":"Mary", "age":20}]'

obj = json.loads(score)  # 將json字串轉為json物件
print(type(score))
print(obj.get('國文'))

obj2 = json.loads(students)
print(type(obj2))
for st in obj2:
    print(st.get('name'), st.get('age'))
