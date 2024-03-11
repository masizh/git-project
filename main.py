# 3 add begirad va az bozorg be kochak moratab kond
num1=int(input('please enter a number:'))
num2=int(input('please enter a number:'))
num3=int(input('please enter a number:'))
max_num = num1
main=num2
min_num = num3

if num2>max_num:
    max_num=num3
    
elif num2<min_num:
    min_num = num2
    
else:
    min_num = num3
    
    if num1<max_num & num1>min_num:
        main=num1
        
    elif num2<max_num & num2>min_num:
        main=num2
        
    else:
        main=num3
        print(max_num,main,min_num)