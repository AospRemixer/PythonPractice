from math import *
import statistics

#Input List
first_list = input('List: ')
final_list = list(map(int, first_list.split()))
final_list = [int(number) for number in final_list]
print(final_list)

#Mean
mean_main = float(statistics.mean(final_list))
print(f"The Mean Is [{mean_main}]")

#Median
median_main = float(statistics.median(final_list))
print(f"The Median Is [{median_main}]")

#Mode
mode_main = statistics.multimode(final_list)
print(f"The Mode Is {mode_main}")

#Range
bignum = max(final_list)
smallnum = min(final_list)
range_main = bignum - smallnum
print(f"The Range Is [{range_main}]")

#Minimum 
print(f"The Minimum Is [{smallnum}]")

#Maximum
print(f"The Maximum Is [{bignum}]")

#Sum
sum_main = sum(final_list)
print(f"The Sum Is [{sum_main}]")

#Count
len_main = len(final_list)
print(f"The Count Is [{len_main}]")

#Quartiles
def quar_1():
    return (len_main + 1) * 0.25
quar_main = quar_1()
print(f"The Quartile 1 is [{quar_main}]")

#Quartiles
def quar_2():
    return (len_main + 1) * 0.50
quar_main_2 = quar_2()
print(f"The Quartile 2 is [{quar_main_2}]")

#Quartiles
def quar_3():
    return (len_main + 1) * 0.75
quar_main_3 = quar_3()
print(f"The Quartile 3 is [{quar_main_3}]")