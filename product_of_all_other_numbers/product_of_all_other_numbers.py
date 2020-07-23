'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    
#init empty arr that will store multiplied values (except THAT one)
#setup indexes that will be removed
    #make a new array for every i that will have all values from arr
    #pop off the value from of index i
    #initialize product as 1
    #for each value in my_list, multiply them (remember, at this point we have removed THAT value)
        #multiply current integer with product
    #once iteration is finished, append that product to answers

    answers = []
    for i in range(len(arr)):
        my_list = list(arr)
        my_list.pop(i)
        product = 1
        for integer in my_list:
            product *= integer
        answers.append(product)
    return answers

    # init empty arr that will store multiplied values (except THAT one)
    # answers = []
    # for i in range(len(arr)):
    #     curr = arr[i]
    #     my_list = [x for x in arr if x != curr]
    #     print(my_list)
    #     product = 1
    #     for integer in my_list:
    #         product *= integer
    #     answers.append(product)
    # print('ANSWERS: ', answers)
    # return answers

product_of_all_other_numbers([1, 2, 3, 4, 5])

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    # print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
