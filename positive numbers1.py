list1 = [12, -7, 5, 64, -14]
list2=[12,14,-95,3]
num = 0
num1=0 
  
while(num < len(list1)):
     
    
    if list1[num] >= 0:
        print(list1[num], end = " ")
     
    
    num += 1
while(num1 <len(list2)):
    
    if list2[num1]>=0:
        print("\t")
        print([list2[num1]],end="")
        
    num1+=1
