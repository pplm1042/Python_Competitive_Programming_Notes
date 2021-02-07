import json

# 사전 자료형(dict) 데이터 선언
user = {
    "id" : "gildong",
    "password" : "192837",
    "age" : 30,
    "hobby" : [
        "football" ,
        "programming"
    ]
}

# JSON 데이터로 변환하여 파일로 저장
with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file, indent = 4)