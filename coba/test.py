a = 'hshdjhsh'
b = [0]*len(a)
x = 0
for i in a:
    b[x] = i
    x+=1
b.sort()
c = ""
for j in b:
    c + j
print(c)