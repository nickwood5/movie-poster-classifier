import csv, json

def create_dictionary(csv_name, output_file_name):
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

    
            genres.append(genre_1)
        

            genres.append(genre_2)
        

            genres.append(genre_3)

            database[r+1] = genres

        with open(output_file_name + ".json", "w") as outfile:
            json.dump(database, outfile)


create_dictionary('Testing', 'testing_lookup')
create_dictionary('Training', 'training_lookup')
create_dictionary('Verification', 'validation_lookup')