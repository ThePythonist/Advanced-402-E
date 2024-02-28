import csv


def write(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name","Field","Grade"])
        writer.writerows(data)

    print(f'{filename} has been created successfully.')


stds = [
    ["Hassan", "Graphic", 15],
    ["Alireza", "Shimi", 19],
    ["Leila", "Computer", 17],
    ["Shayan", "Computer", 14],
]

write("students.csv", stds)
