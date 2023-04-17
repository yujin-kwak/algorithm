
n = int(input())
for i in range(n):
    s = input()
    s = s.upper() # 대소문자 구분 안하므로 전부 대문자로 변경
    size = len(s)
    for j in range(size//2): # s문자열 길이의 절반만 본다.
        if s[j] != s[-1-j]: # 회문 아님
            print("#{0} NO".format(i+1))
            break
    else:
        print("#{0} YES".format(i + 1))

'''
n = int(input())
for i in range(n):
    s = input()
    s = s.upper() # 대소문자 구분 안하므로 전부 대문자로 변경
    if s == s[::-1]: # s의 reverse가 됨.
        print("#{0} YES".format(i + 1))
    else:
        print("#{0} NO".format(i + 1))
'''