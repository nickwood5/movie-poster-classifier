from turtle import down
import download_dataset_2, os

data_set = "remove_bad_images/training"

all_files = os.listdir(data_set)

for file in all_files:
    #print(file)
    image_name = file[:-4]
    #print(image_name)
    a = download_dataset_2.verify_image(data_set, image_name)