a = {}

a[1] = 2

print(a)
import csv

def create_dictionary(csv_name):
    database = {}
    with open(csv_name + '.csv', 'r', encoding="utf-8") as csvfile:
        data = csv.reader(csvfile)
    
    rows = []

    for row in data:
        rows.append(row)

    for r in range (0, len(rows)):

        row = rows[r]
        genre_1 = row[2]
        genre_2 = row[3]
        genre_3 = row[4]

        genres = []

        if genre_1 != "":
            genres.append(genre_1)
        
        if genre_2 != "":
            genres.append(genre_2)
        
        if genre_3 != "":
            genres.append(genre_3)

        database[r] = genres