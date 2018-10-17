##99乘法表##
# 左下三角
print("左下三角：")
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}*{}={:<3d}".format(j, i, j * i), end=" ")
    print("\n")

#############
# 矩形
print("\n矩形：")
for i in range(1, 10):
    for j in range(1, 10):
        print("{}*{}={:<3d}".format(j, i, j * i), end=" ")
    print('\n')

#################
# 左上
print("\n左上三角：")
for i in range(1, 10):
    for j in range(i, 10):
        print("{}*{}={:<3d}".format(i, j, j * i), end=" ")
    print("\n")

############3
# 右上(右边不齐)
print("\n右上三角：")
for i in range(1, 10):
    for k in range(1, i):
        print(end="       ")
    for j in range(i, 10):
        print('{}*{}={:>3d}'.format(i, j, i * j), end='  ')
    print("\n")

#############
# 右下(右边不齐)
print("\n右下三角：")
for i in range(1, 10):
    for k in range(i, 10):
        print(end='       ')
    for j in range(1, i + 1):
        print('{}*{}={}'.format(i, j, i * j), end='  ')
    print('\n')

###############
