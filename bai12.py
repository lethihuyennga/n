# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:13:12 2024

@author: PC
"""

#Viết một hàm để tạo ra một số nguyên ngẫu nhiên từ 1 đến 1000. Sau đó, kiểm tra xem số
#đó có phải là số nguyên tố hay không.
#Số nguyên tố là số nguyên dương lớn hơn 1 và chỉ có hai ước số dương là 1 và chính nó.
import random
def question_12():
    n=random.randint(1,1000)
    if n<1:
        return n,False
    if n==2:
        return n,True
    if n>2:
        for i in range(2,n):
          if  n%i==0:
            return n,False
        else:
            return n,True
print(question_12())