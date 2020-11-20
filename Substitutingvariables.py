def solution(value):
    return "Value is "+("0"*(5-len(str(value))))+str(value)

txt = "50"
x = txt.zfill(10)
print(x)