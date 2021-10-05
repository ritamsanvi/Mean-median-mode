import csv

with open("SOCR-HeightWeight.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data =[]

for i in range(len(file_data)):
    n_num= file_data[i][1]
    new_data.append(float(n_num))


# Median

new_data.sort()

n = len(new_data)

if(n % 2 == 0):
    first_num = new_data[n//2]
    second_num = new_data[(n +1)//2]
    median = (first_num+second_num)/2
else:   
    median = new_data[n//2]


print("Median value of Height is ", median)