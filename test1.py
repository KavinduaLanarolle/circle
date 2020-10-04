total=0      #total of credits
pass_m=0     #pass_m=pass marks
defer=0      #defer marks
fail=0       # fail marks
x=[0,20,40,60,80,100,120]    #range
while total<=120:
    try:
        print('******credits are in the range 0,20,40,60,80,100,120******')
        pass_m=int(input('Input the credits at pass : '))  
        defer=int(input('Input the credits at defer: '))
        fail=int(input('Input the credits at fail : '))
        total=pass_m+defer+fail
        if pass_m in x and defer in x and fail in x :
            if pass_m==120:
                print('Progress')
                num_rows = int(input("Enter the number of rows"));
                for i in range(0, num_rows):
                    for j in range(0, num_rows-i-1):
                        print(end=" ")
                        for j in  range(0, i+1):
                            print("*", end=" ")
                    print()
                
            elif pass_m==100:
                print('Progress-module trailer')
            elif pass_m<=80 and fail<=60:
                print('Do not progress')
            elif pass_m<=40 and fail>=80:
                print('Exclude')
        else:
            print('Range error')
    except:
        print('Intergers required')
else:
    print('Total incorrect')

