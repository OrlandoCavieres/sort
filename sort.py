def get_pivot(array, i, j):
	pivot = array[j]
	item = i - 1

	for k in range(i, j):
		if array[k] <= pivot:
			item = item + 1
			(array[item], array[k]) = (array[k], array[item])

	array[item + 1], array[j] = array[j], array[item + 1]

	return item + 1

def quick_sort(array, i=0, j=None):
    if j == None:
        j = len(array) - 1
    def _quick_sort(array, i, j):
        if i >= j:
            return
			
        pivot = get_pivot(array, i, j)
        _quick_sort(array, i, pivot-1)
        _quick_sort(array, pivot+1, j)
    return _quick_sort(array, i, j)

def bubble_sort(array):
    array_len = len(array)

    for i in range(array_len-1):
        for j in range(0, array_len-i-1):
            if array[j] > array[j + i]:
                array[j], array[j + 1] = array[j + 1], array[j]

def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key
