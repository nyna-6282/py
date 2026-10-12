def unique_int():
    try:
        numbers=list(map(int,input("ENTER A LIST OF INTEGERS SEPARATED BY SPACES : ").split()))
        unique_num=[]
        for num in numbers :
            if num in unique_num:
                raise ValueError("DUPLICATE VALUES FOUND : ",num)
            unique_num.append(num)
        print("ALL NUMBERS ARE UNIQUE..")
    except ValueError as e :
        print("ERROR ",e)
unique_int()
