import re     # regulation expression 약어

# 뺑소니 목격한 차량의 번호판이 4자리 영문자 ca?e 일 때
p = re.compile('st$')    
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case | caffe는 안됨
# ^ (^de) : 문자열의 시작 > desk, destination | fade는 안됨
# $ (se$) : 문자열의 끝 > case, base | face는 안됨

def print_match(m) :
    if m :    # 들어온 값이 있는 경우
        print("m.group() :", m.group())  # 일치하는 문자열(p) 반환 
        print("m.string :", m.string)    # 입력받은 문자열('pianist') 그대로 반환
        print("m.start() :", m.start())  # 일치하는 문자열의 시작 index
        print("m.end() :", m.end())      # 일치하는 문자열의 끝 index
        print("m.span() :", m.span())    # 일치하는 문자열의 시작과 끝의 index
    else :    # 들어온 값이 None인 경우
        print('매칭되지 않았습니다.')

# m = p.match('pianist')    # 정규식과 매칭여부 판단
# print(m)
# print_match(m)

m = p.search("pianist")   # search: 주어진 문자열 중에 일치하는게 있는지 확인
print(m)
print_match(m)

# list = p.findall("small cake case")     # 일치하는 모든 것을 리스트 형태로 반환
# print(list)