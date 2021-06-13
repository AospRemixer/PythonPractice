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
range_main = (final_list)
print(f"The Range Is [{range_main}]")