# Assignment 14

#Given a dictionary where keys are the names of bus stops and values are lists of timestamps (in minutes past 8:00 a.m.)that the bus arrives at that stop, 
#write a function that takes a bus stop name and a time, 
#and returns the number of minutes until the bus arrives at that stop. If the bus does not come again on that day, return -1. 

#Task 1
def jaccard_similarity(setA, setB):
    
    intersection = len(setA.intersection(setB))
    
   
    union = len(setA.union(setB))
    
    
    similarity = intersection / union if union != 0 else 0  
    
    return similarity


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(jaccard_similarity(set1, set2))

#Task 2

a3_bus = {
    'University Ave & 27th Ave SE': [0, 10, 20, 30, 40, 50],
    'University Ave & Oak St': [3, 13, 23, 33, 43, 53],
    'Washington Ave & Pleasant St SE': [6, 16, 26, 36, 46, 56],
    'Washington Ave SE & Union St SE': [7, 17, 27, 37, 47, 57],
    'Fulton St SE & Delaware St SE': [8, 18, 28, 38, 48, 58],
    'Harvard St SE & Delaware St SE': [9, 19, 29, 39, 49, 59],
}

def bus_timing(bus_stop, minutes):
    
    if bus_stop not in a3_bus:
        return "This bus name is not on the list"

    
    timestamps = a3_bus[bus_stop]

    
    for t in timestamps:
        if t >= minutes:
            
            return t - minutes
    
    
    return -1

def test_bus_timing():
    result1 = bus_timing('University Ave & 27th Ave SE', 8)
    assert result1 == 2, f"Expected 2, got {result1}"

    result2 = bus_timing('University Ave & 27th Ave SE', 9)
    assert result2 == 1, f"Expected 1, got {result2}"

    result3 = bus_timing('University Ave & 27th Ave SE', 10)
    assert result3 == 0, f"Expected 0, got {result3}"

    result4 = bus_timing('University Ave & 27th Ave SE', 51)
    assert result4 == -1, f"Expected -1, got {result4}"

    
    result5 = bus_timing('Nonexistent Stop', 25)
    assert result5 == "This bus name is not on the list", f"Expected 'This bus name is not on the list', got {result5}"


test_bus_timing()

#Task 3
students_courses = {
    'Daniel': {'Introduction to Python', 'Sociology 101'},
    'Marina': {'History for Dummies', 'Introduction to Python'},
    'Oleg': {'Matrix Escape', 'Sociology 101'},
    'Moishe': {'Introduction to Python', 'History for Dummies'},
    'Bram': {'Matrix Escape', 'Sociology 101', 'History for Dummies'},
    'Izya': {'Matrix Escape', 'Introduction to Python'}
}
def find_common_courses(student1, student2, database):
   
    courses1 = database.get(student1)
    courses2 = database.get(student2)
    
    
    if courses1 is None or courses2 is None:
        return "One or both of the student names are not in the database."
    
    
    common_courses = courses1.intersection(courses2)
    
    
    if not common_courses:
        return "No common courses."
    
    
    return list(common_courses)

print(find_common_courses('Oleg', 'Bram', students_courses))
print(find_common_courses('Oleg', 'Moishe', students_courses))  
print(find_common_courses('Daniel', 'Benchik', students_courses))  

#Task 4

def shortest_route(subway_system, start, end):
    visited = set()  
    queue = [start]  
    path = {start: [start]}  

    while queue:
        current_station = queue.pop(0)  
        visited.add(current_station)  

        for neighbor in subway_system[current_station]:
            if neighbor not in visited:
                if neighbor not in path:
                    path[neighbor] = path[current_station] + [neighbor]

                if neighbor == end: 
                    return path[neighbor]

                queue.append(neighbor)

    return None  


subway_system = {
    'Station A': {'Station B'},
    'Station B': {'Station A', 'Station C', 'Station D'},
    'Station C': {'Station B', 'Station D', 'Station E'},
    'Station D': {'Station B', 'Station C', 'Station E', 'Station F'},
    'Station E': {'Station C', 'Station D', 'Station F'},
    'Station F': {'Station D', 'Station E'}
}

print(shortest_route(subway_system, 'Station A', 'Station F'))
