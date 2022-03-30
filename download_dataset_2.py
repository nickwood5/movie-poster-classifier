import csv, requests, os, shutil
from PIL import Image

def download_image(target_folder, image_name, image_link):
    img_data = requests.get(image_link).content
    with open(target_folder + '/' + image_name+ '.jpg', 'wb') as handler:
        handler.write(img_data)

def verify_image(target_folder, image_name):
    try:
        img = Image.open('./' + target_folder + '/' + image_name + '.jpg')
        img.verify()
    except OSError:
        print("{} is badly formatted".format(image_name))
        return False
    return True

def download_dataset(target_folder, csv_name):
    with open(csv_name + '.csv', 'r', encoding="utf-8") as csvfile:
        data = csv.reader(csvfile)
        rows = []

        for row in data:
            rows.append(row)

        for r in range (0, len(rows)):

            row = rows[r]
            poster_link = row[5]

            image_name = str(r + 1)
            print("Download image {}".format(image_name))
            download_image(target_folder, image_name, poster_link)
            good_image = verify_image(target_folder, image_name)

            if not good_image:
                os.remove(target_folder + '/' + image_name + '.jpg')
                print("Remove {}".format(image_name))
            

# Test code to download images from sample csvs
#download_dataset('data/sample_test', 'Testing')




#verify_dataset('Training')


download_dataset('cleaned_data/testing', 'Testing')
#download_dataset('cleaned_data/training', 'Training')
#download_dataset('cleaned_data/validation', 'Verification')