lines = ["This is line1\n", "This is line2\n", "This is line3\n"]
with open(
        "C:\\Users\\choig\\Documents\\AIX0004\\04주차_데이터 불러오기 및 Numpy 라이브러리\\04주차_2__Open - Write Files\\text_new2.txt",
        "w") as file2:
    print(file2.name)
    for line in lines:
        file2.write(line)
