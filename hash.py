data = ["","","","","","","","","",""]
run = "Y"
def get_list(key,val,num):
    global data
    Data = {key:val}
    if data[num] == "":
        data[num]=Data
    else:
        count = -1
        for i in data:
            count+= 1
            if i == "":
                data[count] = Data
                break
    return data

def Test_hash(Key):
    numindex = hash(Key)%10
    if numindex >= 10 :
        numindex = numindex % 10
    return numindex
while run == "Y":
    print("1.INSERT")
    print("2.SEARCH")
    print("3.EXIT")
    enter = input("Enter choice : ")
    if enter == "1":
        go1 = "Y"
        while go1 == "Y":
            if "" not in data:
                print("List is full")
                go1 ="N"
            key = input("Enter name : ")
            val = input("Enter ID : ")
            num = Test_hash(key)
            get_list(key,val,num)
            go1 = input("Do more input : Y=yes ,N=no : ")
    elif enter == '2':
        go2= "Y"
        while go2 == 'Y':
            key = input('Enter name : ')
            num = Test_hash(key)
            if key in data[num]:
                print("Your ID : ",data[num].get(key))
            else:
                for i in data:
                    if key in i:
                        print("your ID : ",i.get(key))
                        break
            go2 = input("Do more input : Y=yes ,N=no : ")
    else:
        run = "N"
