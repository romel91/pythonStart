def sort_numbers(numbers,order):
    if order == 'asc':
        return sorted(numbers)
    elif order == 'desc':
        return sorted(numbers,reverse=True)
    elif order == 'none':
        return numbers
    else:
        raise ValueError("Invalid order. Use 'asc' ,'desc' or 'none'.")
    
input_numbers =[3,1,4,1,5,9,2,6,5,3,5]        
order_type ='desc'
sorted_list =sort_numbers(input_numbers ,order_type)
print(f"Orginal list: {input_numbers}")
print(f"Sorted list ({order_type}): {sorted_list}")
