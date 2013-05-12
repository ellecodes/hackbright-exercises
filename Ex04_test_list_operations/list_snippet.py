def custom_len(input_list):
    """custom_len(input_list) imitates len(input_list)"""
    length = 0
    for a in input_list:
        length += 1 

    #a = input_list[-1], 
    #length = (input_list[a.index] + 1)
    # print length
    return length

list = [1, 2, 3]
custom_len(list)