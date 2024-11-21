'''
print the following

*
**
***
****
*****
*/
'''
'''
 *      *
  *    *
   *  *
    *
   *  *
  *    *
 *      *
*        *

'''


i = 1
j = 1

while i<=5 :

    while  j <=5:
        print ("*" * j)
        j = j + 1
    i += 1
print ("--------------------------------")
i = 1
j = 8
k = 5

while i<=7:
    while j > ((int (i / 2))) :
       # print ("*" * j)
       if j >i:
           print (" "*i +"*"+" "*(j-i)+"*")
           j =  j-1
           i += 1
       else:
           print (" "*(i) +"*")
           j = j - 1
           i += 1

    while k >1:
         if i > k:
            print(" " * (k-1) + "*" + " " * (i-k) + "*")
            k = k-1
            i = i +1
         else:
            k = k - 1
            i += 1






