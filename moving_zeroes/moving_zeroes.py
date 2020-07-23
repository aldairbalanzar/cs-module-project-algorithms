'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    #iterate through arr
    for i in arr:
    #is i == 0
        if i == 0:
        #if so, move to end of arr
            arr.append(i)
            arr.remove(i)
    return arr

moving_zeroes([2, 0, 3, 0, 5])

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")