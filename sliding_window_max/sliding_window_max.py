'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(arr, k):
    # init sub-arr the length of k
    # iterate through sub-arr and find max
    # increase shift the indexes of sub-arr one to the right
    window = []
    for index in range(len(arr[:-1*(k-1)])):
        window.append(max(arr[index:index+k]))
    return window
    
print(sliding_window_max([2, 4, 6, 8, 10], 3))

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
