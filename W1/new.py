with open("a.txt") as fh:
    team = fh.readlines()
    
num = 0
    
for i  in range(len(team)):
    a = team[i].strip().split() #strip()去除(頭/尾)空白, split()分割
    
    if i%1 == 0:     
        num += 1
        print("第" + str(num) + "組:",a[0:3])
        
    if i%1 == 0:
        num += 1
        print("第" + str(num) + "組:",a[3:6])
        
    if i%1 == 0:
        num += 1
        if num == 15:   #如果跑到15就取消
            break
        else:            
            print("第" + str(num) + "組:",a[6:9])
    

    