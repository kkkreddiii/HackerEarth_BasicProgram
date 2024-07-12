x = input().strip()
count_z = x.count('z')
count_o = x.count('o')

if count_o == 2 * count_z:
    print("Yes")
else:
    print("No")
