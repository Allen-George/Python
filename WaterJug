from collections import defaultdict

jug_1 = 4
jug_2 = 3

target = 2

visited = defaultdict(lambda: False)

def waterjug(amount_1,amount_2):
    if (amount_1 == target and amount_2 == 0) or (amount_2== target and amount_1== 0):
        print(amount_1,amount_2)
        return True
    
    if visited[(amount_1,amount_2)] == False:
        print(amount_1,amount_2)
        
        visited[(amount_1,amount_2)] = True
        return(waterjug(0,amount_2) or
               waterjug(amount_1,0) or
               waterjug(jug_1,amount_2) or
               waterjug(amount_1,jug_2) or
               waterjug(amount_1 + min(amount_2, (jug_1-amount_1)), amount_2 - min(amount_2, (jug_1-amount_1))) or
               waterjug(amount_1 - min(amount_1,(jug_2-amount_2)),amount_2 + min(amount_1,(jug_2-amount_2))))
               
    else:
        return False
    
print("Steps:")

waterjug(0,0)
