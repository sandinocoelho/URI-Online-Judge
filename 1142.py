tests = int(input())
count = 1
for x in range(tests*4):
    if count % 4 == 0:
        print("PUM")
    else:
        print("%d " %(count), end="")
    count += 1