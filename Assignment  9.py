
#task 1
import random

capitals = {
    'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin',
    'Italy': 'Rome', 'USA': 'Washington', 'Canada': 'Ottawa',
    'Switzerland': 'Bern', 'Austria': 'Vienna',
    'Belgium': 'Brussels', 'Sweden': 'Stockholm',
    'Norway': 'Oslo', 'Denmark': 'Copenhagen',
    'Finland': 'Helsinki', 'Poland': 'Warsaw',
    'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens'
}

score = 0

print("Guess the capital of the country. To exit the game, type 'exit'.")

while True:
    random_country = random.choice(list(capitals.keys()))
    print(random_country)
    answer = input("Please write the capital:")

    if answer.lower() == "exit":
        print(f"Your final score is: {score}")
        break  
    elif answer.lower() == capitals[random_country].lower():
        print("You are right!")
        score += 1
    else:
        print(f"Wrong! The capital of {random_country} is {capitals[random_country]}")

    print(f"Current score: {score}")



# Task 4
def majority_element(nums: list) -> int:
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

def test_majority_element():
    result1 = majority_element([3, 2, 3])
    assert result1 == 3

    result2 = majority_element([2, 2, 1, 1, 1, 2, 2])
    assert result2 == 2

    print("All tests passed!")

test_majority_element()  


# Task 5
def get_subjects_not_passed_by_all_students(student_exams):
    subjects = set(subject for _, _, subject in student_exams)
    subjects_not_passed_by_all = set()

    for subject in subjects:
        # Check if all students failed the subject
        if all(score < 60 for _, score, subj in student_exams if subj == subject):
            subjects_not_passed_by_all.add(subject)

    return subjects_not_passed_by_all

def test_get_subjects_not_passed_by_all_students():
    exams = [
        ("Alice", 55, "Math"),
        ("Bob", 40, "Math"),
        ("Charlie", 30, "Math"),
        ("Alice", 50, "Science"),
        ("Bob", 45, "Science"),
        ("Charlie", 40, "Science"),
        ("Alice", 95, "History"),
        ("Bob", 85, "History"),
        ("Charlie", 90, "History"),
    ]

    assert get_subjects_not_passed_by_all_students(exams) == {"Math", "Science"}

    print("Test passed!")

test_get_subjects_not_passed_by_all_students()
