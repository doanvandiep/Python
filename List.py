X, Y, Z, n = [int(input().strip()) for i in range(4)]
print([ [x,y,z]
       for x in range(X+1)
       for y in range(Y+1)
       for z in range(Z+1)
       if x + y + z !=n])