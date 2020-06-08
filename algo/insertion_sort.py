def insertion_sort(number_list):
    '''
    always assumes left side of the key is already sorted.
    therefore we are checking where to place new key value in the sorted left side array.
    '''
    for i in range(1,len(number_list)):
        key = number_list[i] #as the loop starts from 1, assumes leftmost value is already sorted.
        j = i-1 #last index of the sorted sub array.
        while j >= 0 and number_list[j] >key: #loops from end of the sorted part to begining and determine where to place the key.
            number_list[j+1] = number_list[j] #while current_value_in_the_list > key, shift current value to the right.
            j = j-1
        number_list[j+1] = key #place the key in the new position after shifting values.
    return(number_list)


print(insertion_sort([5,2,4,6,1,3]))
