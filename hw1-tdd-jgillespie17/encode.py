def encode (input_string):
    output_list = {}
    output = ""
    for x in input_string:
        if x in output_list:
            output_list[x] = output_list[x]+1
        else: 
            output_list[x] = 1
    for char, value in output_list.items():
        if value == 1:
            output = output + str(char)
        else:
            output = output + str(char) + str(value)
    return output        
