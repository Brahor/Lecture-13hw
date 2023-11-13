def compute_difference(list1, list2):
    result1 = []
    result2 = list2.copy()

    for item in list1:
        if item in result2:
            result2.remove(item)
        else:
            result1.append(item)

    return result1, result2


result1 = compute_difference(['a', 'b', 'c', 'c', 'd'], ['c', 'd', 'e'])
assert result1 == (['a', 'b', 'c'], ['e'])

result2 = compute_difference([], ['c', 'd', 'e'])
assert result2 == ([], ['c', 'd', 'e'])

result3 = compute_difference([1, 2, 3], [4, 4, 5, 6])
assert result3 == ([1, 2, 3], [4, 4, 5, 6])

result4 = compute_difference([1, 2, 3], [2, 3, 4])
assert result4 == ([1], [4])

# Print the results
print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)
print("Result 4:", result4)



#task 2
def sum_of_two(nums: list, target: int) -> list:
    num_dict = {} 
    for idx, num in enumerate(nums):
        difference = target - num
        if difference in num_dict:
            return [num_dict[difference], idx]
        num_dict[num] = idx

def test_sum_of_two():
    result1 = sum_of_two([2,7,11,15], 9)
    assert result1 == [0, 1]

    result2 = sum_of_two([3,2,4], 6)
    assert result2 == [1, 2]

    result3 = sum_of_two([3,3], 6)
    assert result3 == [0, 1]

    print("All tests passed!")

test_sum_of_two()

#task 3 
def unique_elements(arr: list) -> list:
    
    count_dict = {}
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1

    
    return [num for num, count in count_dict.items() if count == 1]

def test_unique_elements():
    result1 = unique_elements([1, 2, 3, 2, 4, 5, 5])
    assert result1 == [1, 3, 4], f"Expected [1, 3, 4] but got {result1}"
    print("Test 1 passed!")

    result2 = unique_elements([1, 2, 3, 4, 5])
    assert result2 == [1, 2, 3, 4, 5], f"Expected [1, 2, 3, 4, 5] but got {result2}"
    print("Test 2 passed!")

    result3 = unique_elements([1, 1, 1, 1, 1])
    assert result3 == [], f"Expected [] but got {result3}"
    print("Test 3 passed!")

test_unique_elements()

#task 4
def odd_elements(arr: list) -> list:
    
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    return [num for num, count in count_dict.items() if count % 2 == 1]

# Test cases with print statements
def test_odd_elements():
    result1 = odd_elements([1, 2, 3, 2, 4, 5, 5])
    print(f"Input: [1, 2, 3, 2, 4, 5, 5], Expected Result: [1, 3, 4], Actual Result: {result1}")
    assert result1 == [1, 3, 4], f"Expected [1, 3, 4], but got {result1}"

    result2 = odd_elements([1, 2, 3, 2, 4, 5, 5, 6, 6])
    print(f"Input: [1, 2, 3, 2, 4, 5, 5, 6, 6], Expected Result: [1, 3, 4], Actual Result: {result2}")
    assert result2 == [1, 3, 4], f"Expected [1, 3, 4], but got {result2}"

test_odd_elements()

# task 5
def second_largest_element(arr: list) -> int:
    
    if len(set(arr)) < 2:
        return None

    biggest = max(arr)
   
    if arr.count(biggest) > 1:
        return biggest
    
    
    without_biggest = [x for x in arr if x != biggest]
    
    return max(without_biggest)

# Testing
def test_second_largest_element():
    result1 = second_largest_element([1, 2, 3, 2, 4, 5,5])
    assert result1 == 5, f"Expected 5, but got {result1}"

    result2 = second_largest_element([1, 2, 3, 4, 5])
    assert result2 == 4, f"Expected 4, but got {result2}"

    result3 = second_largest_element([1, 1, 1, 1, 1])
    assert result3 == None, f"Expected None, but got {result3}"

    print("All tests passed!")

test_second_largest_element()


#task 6
cities = [
    ('New York City', 8550405),
    ('Los Angeles', 3792621),
    ('Chicago', 2695598),
    ('Houston', 2100263),
    ('Philadelphia', 1526006),
    ('Phoenix', 1445632),
    ('San Antonio', 1327407),
    ('San Diego', 1307402),
    ('Dallas', 1197816),
    ('San Jose', 945942),
]

sorted_cities = sorted(cities, key=lambda x: x[1], reverse=True)


total_population = sum(city[1] for city in cities)


average_population = total_population / len(cities)

print("Sorted Cities by Population:")
for city in sorted_cities:
    print(f"{city[0]}: {city[1]}")

print("\nTotal Population:", total_population)
print("Average Population:", average_population)

