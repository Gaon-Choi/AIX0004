file1=open('C:\\Users\\choig\\Documents\\AIX0004\\04주차_데이터 불러오기 및 Numpy 라이브러리\\04주차_1__Open - Reading Files\\text_new.txt', 'r')
print(file1.name)
file_stuff=file1.readlines()
print(file_stuff)
# str이 아닌 리스트 형태로 개별 라인을 저장함.