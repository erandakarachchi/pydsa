def sentinel_linear_search(data_set,search_key):
    data_set_length = len(data_set);
    last_elem = data_set[data_set_length-1]
    data_set[data_set_length-1] = search_key

    print(data_set)
    i =0
    while not search_key == data_set[i]:
        i +=1

    data_set[data_set_length-1] = last_elem

    if (i < (data_set_length-1)) or (last_elem == data_set[data_set_length-1]):
        return i
    else:
        return "Not found"


print("List Index : ",sentinel_linear_search(["John","Doe","Jane","Andy","Mark","Kate"],"Jane"))
