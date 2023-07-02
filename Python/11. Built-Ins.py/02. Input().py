import re
x,k = input().split(" ")
sum_ = 0
string = input()
signs = re.findall('[\+\-]',string)
new_string = re.sub('\-','\+',string)

for i,t in enumerate(new_string.split(' + ')):
    coef = re.findall(r'\d+(?=x)',t)
    if len(coef)==0:
        if re.fullmatch('\d+',t):
            coef = re.findall('\d+',t)[0]
        else:
            coef = 1
    else:
        coef = coef[0]
    
    power = re.findall(r'(?<=x\*\*)\d',t)
    if len(power)==0:
        if re.findall('x',t):
            power =[1]
        else:
            power =[0]
    
    if i>0 and signs[i-1]=='-':
        sum_-= int(str(coef))*(int(str(x))**int(str(power[0])))
    else:
        sum_+= int(str(coef))*(int(str(x))**int(str(power[0])))
                
print(True if sum_ == int(k) else False)