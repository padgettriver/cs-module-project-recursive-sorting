# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    a_counter = 0
    b_counter = 0

    for i in range(0, elements):
        if a_counter == len(arrA) or b_counter == len(arrB):   # if one side runs out of numbers
            if a_counter == len(arrA):
                merged_arr[i] = arrB[b_counter]
                b_counter += 1
            else:
                merged_arr[i] = arrA[a_counter]
                a_counter += 1
        else:                                                 # compare and add lowest number
            if arrA[a_counter] < arrB[b_counter]:
                merged_arr[i] = arrA[a_counter]
                a_counter += 1
            else:
                merged_arr[i] = arrB[b_counter]
                b_counter += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    start = 0
    end = len(arr)
    if end > start + 1:
        mid = int((start + end) / 2)
        arrA = merge_sort(arr[0:mid])
        arrB = merge_sort(arr[mid:end])
        arr = merge(arrA, arrB)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass