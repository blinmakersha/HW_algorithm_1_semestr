# эта функция определяет пары чисел в списке, разность которых является наименьшей. сложность: O(n log n).

def minimumAbsDifference(arr):
    arr.sort()      # отсортировываем исходный список
    min_different_arr = []
    different = 0
    for i in range(0, len(arr)-1):      # создаем цикл, который найдёт минимальную разность между парами цифр
        if different == 0: 
            different = arr[i+1] - arr[i]
        if arr[i+1] - arr[i] < different:
            different = arr[i+1] - arr[i]

    for i in range(0, len(arr)-1):      # создаем цикл, который выводит пары чисел с минимальной разностью
        if arr[i+1] - arr[i] == different:
            min_different_arr.append( [arr[i], arr[i+1]] )
    return min_different_arr

print(minimumAbsDifference([1, 4, 9, 25, 3, 26]))