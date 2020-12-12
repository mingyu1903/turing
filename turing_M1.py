# -*- coding: utf-8 -*-

# 转移函数q1
def q1(w):
    s = w[0]
    # 该位置为0
    if s==0:
        w[0] = 1 # 标记带头
        return 1, 2 # 指针右移,返回指针位置和下一个转移函数q2
    # 该位置为#或x
    else:
        return 0, 6 # 返回指针位置和下一个转移函数qreject(q[6])

# 转移函数qreject
def qr():
    print('Reject')

# 转移函数qaccept
def qa():
    print('Accept')

# 转移函数q2
def q2(i, w):
    s = w[i]
    # 该位置为0
    if s==0:
        w[i] = 2 # 删掉0
        i += 1 # 指针右移
        return i, 3 # 返回指针位置和下一个转移函数q3
    # 该位置为x(用2代替x)
    elif s==2:
        i += 1 # 指针右移
        return i, 2 # 返回指针位置和下一个转移函数q2
    # 该位置为#
    else:
        i += 1 # 指针右移
        return i, 0 # 返回指针位置和下一个转移函数qaccept(q[0])


# 转移函数q3
def q3(i, w):
    s = w[i]
    # 该位置为0
    if s==0:
        i += 1 # 指针右移
        return i, 4 # 返回指针位置和下一个转移函数q4
    # 该位置为x(用2代替x)
    elif s==2:
        i += 1 # 指针右移
        return i, 3 # 返回指针位置和下一个转移函数q3
    # 该位置为#
    else:
        i -= 1 # 指针左移
        return i, 5 # 返回指针位置和下一个转移函数q5


# 转移函数q4
def q4(i, w):
    s = w[i]
    # 该位置为0
    if s==0:
        w[i] = 2
        i += 1 # 指针右移
        return i, 3 # 返回指针位置和下一个转移函数q4
    # 该位置为x(用2代替x)
    elif s==2:
        i += 1 # 指针右移
        return i, 4 # 返回指针位置和下一个转移函数q4
    # 该位置为#
    else:
        i += 1 # 指针右移
        return i, 6 # 返回指针位置和下一个转移函数qreject(q[6])

# 转移函数q5
def q5(i, w):
    s = w[i]
    # 该位置为#(用1代替#)
    if s==1:
        i += 1 # 指针右移
        return i, 2 # 返回指针位置和下一个转移函数q2
    # 该位置为0或x
    else:
        i -= 1 # 指针左移
        return i, 5 # 返回指针位置和下一个转移函数q5


# Turing机M1,输入W为一个只含0的字符串并以#结尾
def m1(W):
    # 转换字符串为数组方便操作(用1代替#，用2代替x)
    w = [int(wi) for wi in W[:len(W)-1]]
    w += [1]
    # 转移函数集合(转移函数qaccept记为q[0],qreject记为q[6])
    q = [qa, q1, q2, q3, q4, q5, qr]
    # 起始状态,t为转移函数序号,i为指针位置
    t = 1
    i, t = q1(w)
    # 当没有到达接受状态或拒绝状态时,不断进行转移
    while t!=0 and t!=6:
        i, t = q[t](i, w)
    # 到达接受状态或拒绝状态,输出结果
    q[t]()

#### test ####
if __name__ == '__main__':
    W = '0000000#' # 0*7
    m1(W)
    W = '00000000#' # 0*8
    m1(W)
    W = '000000#' # 0*6
    m1(W)
    W = '0000#' # 0*4
    m1(W)