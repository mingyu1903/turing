# -*- coding: utf-8 -*-
# 第一步：确认输入具有 a+ b+ c+ 的形式
def step1(w):

    # # 转换字符串为数组方便操作(分别用1,2,3,4,9代替a,b,c,d,#,并用0代替x)
    # w = [int(chr(ord(i)-48)) for i in W[:len(W)-1]]
    # w += [9]

    # 起始状态转移函数qs
    def qs():
        s = w[0]
        if s==1:
            w[0] = 7 # 用7标记带头
            return 1, 1 # 指针右移，返回指针位置和转移函数q1
        else:
            return 1, 0 # 指针右移，返回转移函数qrject(记为q[0]),拒绝

    # 转移函数q1,确认 a+ 部分
    def q1(i):
        s = w[i]
        if s==1:
            i += 1 # 指针右移
            return i, 1 # 返回指针位置和转移函数q1
        elif s==2:
            i += 1 # 指针右移
            return i, 2 # 返回指针位置和转移函数q2
        else:
            i += 1 # 指针右移
            return i, 0 # 返回指针位置和转移函数qrject(记为q[0]),拒绝

    # 转移函数q2,确认 b+ 部分
    def q2(i):
        s = w[i]
        if s==2:
            i += 1 # 指针右移
            return i, 2 # 返回指针位置和转移函数q2
        elif s==3:
            i += 1 # 指针右移
            return i, 3 # 返回指针位置和转移函数q3
        else:
            i += 1 # 指针右移
            return i, 0 # 返回指针位置和转移函数qrject(记为q[0]),拒绝

    # 转移函数q3,确认 c+ 部分
    def q3(i):
        s = w[i]
        if s==3:
            i += 1 # 指针右移
            return i, 3 # 返回指针位置和转移函数q3
        elif s==9:
            i -= 1 # 指针左移
            return i, 4 # 返回指针位置,第一步结束
        else:
            i += 1 # 指针右移
            return i, 0 # 返回指针位置和转移函数qrject(记为q[0]),拒绝

    # 拒绝
    def qr():
        print('Reject')

    q = [qr, q1, q2, q3]
    i, t = qs()
    while t!=0 and t!=4:
        i, t = q[t](i)
    if t==0: # 输入被拒绝,不再进行下面的判断
        t = -3
        qr()

    return i, t

def step2(w, i, t):

    # 返回带头转移函数qback
    def qb(i):
        s = w[i]
        if s==7:
            i += 1 # 指针右移
            return i, 0
        else:
            i -= 1 # 指针左移
            return i, 1

    if t!=-3:
        t = 1
        while t==1:
            i, t = qb(i)

    return i, t

def step3(w, i, t):

    # 起点是带头#右边一位
    def qs(i):
        s = w[i]
        if s==1:
            w[i] = 0 # 将a删去
            i += 1 # 指针右移
            return i, 1 
        elif s==2 or s==4:
            i -= 1 # 指针左移
            return i, -2 # 此时只剩下一个a,进行下一步
        else:
            i += 1 # 指针右移
            return i, 0 # 返回指针位置和转移函数qrject(记为q[0]),拒绝

    # 拒绝
    def qr():
        print('Reject')

    def q1(i):
        s = w[i]
        if s==1:
            i += 1
            return i, 1 # 返回指针位置和转移函数q1
        elif s==2:
            w[i] = 4
            i += 1
            return i, 2 # 返回指针位置和转移函数q2
        elif s==4:
            w[i] = 2
            i += 1
            return i, 4 # 返回指针位置和转移函数q4
        else:
            i += 1
            return i, 0 # 返回指针位置和转移函数qrject(记为q[0]),拒绝

    def q2(i):
        s = w[i]
        if s==0 or s==2 or s==4:
            i += 1
            return i, 2
        elif s==3:
            w[i] = 0
            i -= 1
            return i, 3
        else:
            i += 1
            return i, 0

    def q3(i):
        s = w[i]
        if s==2:
            w[i] = 4
            i += 1
            return i, 2
        elif s==1:
            w[i] = 0
            i += 1
            return i, 1
        elif s==0 or s==3 or s==4:
            i -= 1
            return i, 3
        else:
            i += 1
            return i, -1
    
    def q4(i):
        s = w[i]
        if s==4:
            w[i] = 2
            i += 1
            return i, 4
        elif s==0 or s==3:
            i -= 1
            return i, 5
        else:
            i += 1
            return i, 0
    
    def q5(i):
        s = w[i]
        if s==2:
            w[i] = 4
            i += 1
            return i, 2
        else:
            i += 1
            return i, 0

    q = [qr, q1, q2, q3, q4, q5]
    if t!=-3:
        i, t = qs(i)
        while t!=-2 and t!=-1 and t!=0:
            i, t = q[t](i)

        if t==0: # 该输入被拒绝,不再进行第四步判断
            qr()
            return i, -3
        else:
            return i, t
    else:
        return i, t

def step4(w, i, t):

    def qs1(i):
        i += 1
        return i, 0

    def qs(i):
        s = w[i]
        if s==2 or s==4:
            w[i] = 0
            i += 1
            return i, 1
        else:
            i += 1
            return i, 0

    def q1(i):
        s = w[i]
        if s==3:
            w[i] = 0
            i -= 1
            return i, 2
        elif s==0 or s==2 or s==4:
            i += 1
            return i, 1
        else:
            i += 1
            return i, 4

    def q2(i):
        s = w[i]
        if s==7:
            i += 1
            return i, 3
        elif s==2 or s==4:
            w[i] = 0
            i += 1
            return i, 1
        elif s==0 or s==3:
            i -= 1
            return i, 2

    def q3(i):
        s = w[i]
        if s==3:
            i += 1
            return i, 4
        elif s==9:
            i -= 1
            return i, 5
        else:
            i += 1
            return i, 3

    def qr():
        print('Reject')

    def qa():
        print('Accept')

    q = [qs, q1, q2, q3, qr, qa]

    if t != -3:
        if t==-2:
            i, t = qs1(i)
        elif t==-1:
            i, t = qs(i)

        while t!=4 and t!=5:
            i, t = q[t](i)
        
        q[t]()

def m2(W):
    # 转换字符串为数组方便操作(分别用1,2,3,4,9代替a,b,c,d,#,并用0代替x)
    w = [int(chr(ord(i)-48)) for i in W[:len(W)-1]]
    w += [9]

    i, t = step1(w)
    i, t = step2(w, i, t)
    i, t = step3(w, i, t)
    step4(w, i, t)




#### test ####
if __name__ == '__main__':
    # i, t = step1(w)
    # m2(W)
    # m2(W)
    # m2(W)
    W = 'aabbccccc#' # 0*7
    m2(W)
    W = 'aa#' # 0*8
    m2(W)
    W = 'abc#' # 0*6
    m2(W)
    W = 'c#' # 0*4
    m2(W)