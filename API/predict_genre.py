import torch
import torchvision.transforms as transforms
from PIL import Image

loaded_model = torch.load('/home/nickwood5/poster_classifier/nicks_model6.pt')
loaded_model.eval()

classes = ['Action_Adventure', 'Animation', 'Comedy', 'Documentary', 'Drama', 'Horror_Thriller', 'Romance']
data_directory = '/home/nickwood5/poster_classifier/cropped_uploads/'

convert_tensor = transforms.ToTensor()
batch_size  = 100
num_workers = 2

def get_dataloader2(file_name):
  data = []
  poster_image = Image.open(data_directory + file_name)
  poster_tensor = convert_tensor(poster_image)
  poster_genres = ['none', 'test']
  data.append([poster_tensor, poster_genres])

  dataloader = torch.utils.data.DataLoader(data, batch_size=batch_size, num_workers=num_workers, shuffle=False, drop_last=False)

  return dataloader

def normalize_output(output):
  for x in range (0, len(output)):
      if output[x] >= 0.5:
        output[x] = 1
      else:
        output[x] = 0
  return output

def predict(movie_poster_name):
  a = get_dataloader2(movie_poster_name)

  for i, batch_data in enumerate(a):
    images = batch_data[0]

    outputs = loaded_model(images)
    outputs = torch.sigmoid(outputs)

    n = 0
    for output in outputs:
      predicted_genres = []
      output = output.tolist()

      output = normalize_output(output)
      for genre_num in range (0, len(output)):
        if output[genre_num] == 1:
          predicted_genres.append(classes[genre_num])
      n += 1

  return predicted_genres

