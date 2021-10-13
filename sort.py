def get_pivot(array, i, j):
	pivot = array[j]
	item = i - 1

	for k in range(i, j):
		if array[k] <= pivot:
			item = item + 1
			(array[item], array[k]) = (array[k], array[item])

	array[item + 1], array[j] = array[j], array[item + 1]

	return item + 1

#Fix
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

