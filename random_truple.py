import random


# class Random_tuple:
#     """返回包含三个随机数的元组"""
#     def __init__(self,num):
#         self.tuple = []
#         self.num = num


def rn(num):
    tuples=[]
    for i in range(num):
        number = random.randint(0,255)
        tuples.append(number)

    return tuple(tuples)



print(rn(3))


