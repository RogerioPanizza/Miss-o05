#Microatividade 03

array = [25, 39, 44, 77, 1, 66, 53, 97, 34, 20, 85, 64, 59, 76, 100]

for i in range(len(array)):
    var = i
    for j in range(i+1, len(array)):
        if array[i] > array[j]:
            var = j
            
print(array)
