line4 = ["This is line4\n"]
with open(
        "C:\\Users\\choig\\Documents\\AIX0004\\04주차_데이터 불러오기 및 Numpy 라이브러리\\04주차_2__Open - Write Files\\02_write_mode_2\\text_new2.txt",
        "w") as file2:
    print(file2.name)
    for line in line4:
        file2.write(line)
