f = open("./sample_text.txt", "w")
f.write("Test\n")
print("My", "Name", file=f)
f.close()


with open("test.txt", "w") as f:
    f.write("Text")

with open("test.txt", "r") as f:
    print(f.read())

with open("test.txt", "r") as f:
    while True:
        chunk = 2
        line = f.read(chunk)
        print(line)
        if not line:
            break

# 書き込みと読み込みを同時に宣言

s = "onfvowneofnoewofnweonofwe"
with open('test.py', 'w+') as f:
    f.write(s)
    # 書き込み直後はファイルの位置が最後になっている
    f.seek(0)
    print(f.read())

