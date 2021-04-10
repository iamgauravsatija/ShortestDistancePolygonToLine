x = 15
y = 15
print(x, " ", y)
while x <= 45:
    if x < 30:
        x += 1
        y -= 1
    elif x == 30:  
        x += 1
        y += 1
    else:    
        x += 1
        y += 1
    print(x, " ", y)
print("===")
while x > 15:
    if x < 30:
        x -= 1
        y -= 1
    elif x == 30: 
        x -= 1
        y -= 1
    else:   
        x -= 1
        y += 1
    print(x, " ", y)