# import math
from decimal import Decimal
#
# c = [50,20,10,5,2,1,0.50,0.20,0.10,0.05,0.02,0.01]
#
# def changeCalculator(value):
#     for i in c:
#         n = math.floor(value/i)
#         if n>0:
#             if i>=1:
#                 print(str(n)+"x"+" £"+str(i))
#                 print(value-n*i)
#                 value = value -n*i
#             else:
#                 print(str(n)+"x "+str(int(i*100))+"p")
#                 value = value-n*i
#         else:
#             continue

# changeCalculator(100.10)

print(Decimal(100.1)-Decimal(100))