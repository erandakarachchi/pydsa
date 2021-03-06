def nonincreasing_insertion_sort(number_list):
    for key_idx in range(1, len(number_list)):
        key = number_list[key_idx]
        sorted_idx = key_idx -1
        while sorted_idx>=0 and number_list[sorted_idx] < key:
            number_list[sorted_idx+1] = number_list[sorted_idx]
            sorted_idx -=1
        number_list[sorted_idx+1] = key
    return(number_list)

print(nonincreasing_insertion_sort([5,2,4,6,1,3]))
print(nonincreasing_insertion_sort([1,2,3,4,5,6,7]))
print(nonincreasing_insertion_sort([1,2,3,4,43,657,32465,423,46,45,423,756,48,67432,75,2,34,67523,756231,56,86,243,567,423,75632,654,5,6,7]))
