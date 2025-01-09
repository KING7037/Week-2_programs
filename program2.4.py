def distribute_sweets(total_sweets, num_pupils):
    if num_pupils == 0:
        return "Number of pupils cannot be zero."
    
    sweets_per_pupil = total_sweets // num_pupils
    sweets_left_over = total_sweets % num_pupils
    
    return sweets_per_pupil, sweets_left_over

total_sweets = int(input("Enter the total number of sweets: "))
num_pupils = int(input("Enter the number of pupils: "))

result = distribute_sweets(total_sweets, num_pupils)

if isinstance(result, str):
    print(result)
else:
    sweets_per_pupil, sweets_left_over = result
    print(f"Each pupil will receive {sweets_per_pupil} sweets.")
    print(f"Sweets left over: {sweets_left_over}")









