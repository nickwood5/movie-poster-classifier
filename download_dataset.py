import csv, requests

def download_image(target_folder, image_name, image_link):
    img_data = requests.get(image_link).content
    with open(target_folder + '/' + image_name+ '.jpg', 'wb') as handler:
        handler.write(img_data)

# Array of genres
genres = ['Animation', 'Action', 'Comedy', 'Adventure', 'Biography', 'Crime', 'Drama', 'Documentary', 'Sci-Fi', 'Short', 'Fantasy', 'Horror', 'Thriller', 'Romance', 'Mystery',
          'Western', 'Music', 'Sport', 'Family', 'Film-Noir', 'History', 'Musical', 'Talk-Show', 'War']

def download_dataset(target_folder, csv_name):
    with open(csv_name + '.csv', 'r') as csvfile:
        data = csv.reader(csvfile)
        rows = []
        
        # Initialize genre count dict
        genre_counts = {}
        for genre in genres:
            genre_counts[genre] = 0
        
        for row in data:
            rows.append(row)

        for r in range (1, len(rows)):
            poster_link = rows[r][0]
            genre = rows[r][2]
            target_sub_directory = target_folder + '/' + genre
            image_name = genre + '_' + str(genre_counts[genre])
            download_image(target_sub_directory, image_name, poster_link)
            genre_counts[genre] += 1

# Test code to download images from sample csvs
download_dataset('sample_test', 'sample_test_data')
download_dataset('sample_train', 'sample_train_data')
download_dataset('sample_validation', 'sample_validation_data')
