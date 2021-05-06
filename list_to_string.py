####################################
# 배열 내 문자를 문자열로 만들어준다.

char_list = ['1', '2', '3', '4', '5']

list_to_string = "".join(map(str, char_list))

print(list_to_string)