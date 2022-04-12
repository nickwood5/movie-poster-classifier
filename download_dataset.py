import csv, requests, os, shutil
from PIL import Image

def download_image(target_folder, image_name, image_link):
    img_data = requests.get(image_link).content
    with open(target_folder + '/' + image_name+ '.jpg', 'wb') as handler:
        handler.write(img_data)

# Array of genres
#genres = ['Animation', 'Action', 'Comedy', 'Adventure', 'Biography', 'Crime', 'Drama', 'Documentary', 'Sci-Fi', 'Short', 'Fantasy', 'Horror', 'Thriller', 'Romance', 'Mystery',
#          'Western', 'Music', 'Sport', 'Family', 'Film-Noir', 'History', 'Musical', 'Talk-Show', 'War']

# Test array
genres = ['Animation', 'Drama', 'Action_Adventure', 'Horror_Thriller', 'Comedy', 'Romance', 'Documentary']

def verify_image(target_sub_directory, image_name):
    try:
        img = Image.open('./' + target_sub_directory + '/' + image_name + '.jpg')
        img.verify()
    except OSError:
        print("{} is badly formatted".format(image_name))
        return False
    return True

def download_dataset(target_folder, csv_name):
    with open(csv_name + '.csv', 'r', encoding="utf-8") as csvfile:
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
            image_name = genre + '_' + str(genre_counts[genre])
            print("Download image {}".format(image_name))
            download_image(target_sub_directory, image_name, poster_link)
            good_image = verify_image(target_sub_directory, image_name)
            genre_counts[genre] += 1
            if not good_image:
                os.remove(target_sub_directory + '/' + image_name + '.jpg')
                print("Remove {}".format(image_name))

# Test code to download images from sample csvs
#download_dataset('data/sample_test', 'Testing')


def verify_dataset(csv_name):
    genre_counts = {}
    for genre in genres:
        genre_counts[genre] = 0


    with open(csv_name + '.csv', 'r', encoding="utf-8") as csvfile:
        data = csv.reader(csvfile)
        rows = []

        for row in data:
            rows.append(row)

        for r in range (0, len(rows)):
            row = rows[r]
            genre = row[2]
            image_name = genre + '_' + str(genre_counts[genre])
            
            print("Download image {} {}".format(r, image_name))
            genre_counts[genre] += 1

#verify_dataset('Training')


#download_dataset('data/sample_test', 'Testing')
#download_dataset('data/sample_train', 'Training')
download_dataset('data/sample_validation', 'Verification')