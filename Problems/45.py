'''
Triangular, pentagonal, and hexagonal

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	T=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	P=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	H=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''

from itertools import count

def tripetsest(k):
    '''True False'''
    #T=n(n+1)/2
    #P=n(3n−1)/2
    #H=n(2n−1)
    #ubistvu resujem tri kvadratne enacbe
    #(stevilo).is_integer() preveri, ali je float u resnici celo stevilo
    #zaradi hitrosti najprej preverimo hexagonal, nato pentagonal, nato triangle
    return ((1 + (1+8*k)**(1/2))/4).is_integer() and ((1 + (1+24*k)**(1/2))/6).is_integer() and ((-1 + (1 + 8*k)**(1/2)) / 2).is_integer()


for i in count(40756):
    if not i % 10**6: #vsako miljonto stevilo sprinta da vidimo napredek
        print(i)
    if tripetsest(i):
        print(i)
        break

#this gonn be one big number
#00:17 start
#00:46 konec  (1533776805)
