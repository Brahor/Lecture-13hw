# assignment 10

cats_with_hats = [False] * 100


for round_number in range(1, 101):  
    for cat_index in range(len(cats_with_hats)): 
        if (cat_index + 1) % round_number == 0:  
            cats_with_hats[cat_index] = not cats_with_hats[cat_index]  


cats_with_hats_positions = []

for cat_index in range(len(cats_with_hats)):
    
    if cats_with_hats[cat_index]:
        
        cats_with_hats_positions.append(cat_index + 1)


print(cats_with_hats_positions)
