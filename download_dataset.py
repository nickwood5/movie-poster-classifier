import csv, requests, os, shutil

def download_image(target_folder, image_name, image_link):
    img_data = requests.get(image_link).content
    with open(target_folder + '/' + image_name+ '.jpg', 'wb') as handler:
        handler.write(img_data)

# Array of genres
#genres = ['Animation', 'Action', 'Comedy', 'Adventure', 'Biography', 'Crime', 'Drama', 'Documentary', 'Sci-Fi', 'Short', 'Fantasy', 'Horror', 'Thriller', 'Romance', 'Mystery',
#          'Western', 'Music', 'Sport', 'Family', 'Film-Noir', 'History', 'Musical', 'Talk-Show', 'War']

# Test array
genres = ['Animation', 'Drama', 'Action_Adventure', 'Horror_Thriller', 'Comedy', 'Romance', 'Documentary']

def download_dataset(target_folder, csv_name):
    with open(csv_name + '.csv', 'r') as csvfile:
        data = csv.reader(csvfile)
        rows = []
        
        # Initialize genre count dict and subdirectories
        genre_counts = {}
        for genre in genres:
            genre_counts[genre] = 0
            dir = os.path.join(target_folder, genre)
            if (os.path.exists(dir)):
                shutil.rmtree(dir)

            os.mkdir(dir)

        for row in data:
            rows.append(row)

        for r in range (0, len(rows)):

            row = rows[r]
            name = row[0]
            poster_link = row[5]
            genre = row[2]
            year = row[1]


            target_sub_directory = target_folder + '/' + genre
            image_name = name + '_' + year + '_' + genre + '_' + str(genre_counts[genre])
            print("Download image {}".format(image_name))
            download_image(target_sub_directory, image_name, poster_link)
            genre_counts[genre] += 1

# Test code to download images from sample csvs
download_dataset('data/sample_test', 'Testing')
