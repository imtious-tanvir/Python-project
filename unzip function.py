student = [
    (1, 'Imtious', 21),
    (2, 'Tanvir', 23),
    (3, 'Rahi', 25),
    (4, 'Sabrina', 17),
    (5, 'Sathi', 19)
]
unzip = list(zip(*student))
id = unzip[0]
name = unzip[1]
age = unzip[2]
print(f"Student's ID: {id}")
print(f"Student's Name: {name}")
print(f"Student's Age: {age}")
