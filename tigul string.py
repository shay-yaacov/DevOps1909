
s  = "Sometimes, I will meet a road-runner. perhaps - who know"

s = s.replace ("-","$")
print(s)
s= s.replace(" $ "," - ")
print(s)
puncts = ",.-"
for punct in puncts:
   s = s.replace(punct,"")
   print(s)
s= s.replace("$","-")
print(s)

s = "to be or not to be"
s = s.split()
print(s)

mys= ''' from $ a,b c , d
          vvv   '''
print (mys.split('$'))

l = [1,2,3,20,8]
x= len(l)
print(x)
for i in range(3,len(l)):
    print (i)

lst =[2,2,4,10]
sumnum = 0
sums = []
print ("________")
for num in lst[0:5]:
    print (num)
    sumnum = sumnum + num
    sums = sums + [sumnum]
print (sums)



