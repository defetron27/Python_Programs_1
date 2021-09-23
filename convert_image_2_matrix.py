from google.colab import drive, files
import numpy as np

drive.mount("/content/gdrive")

data_drive_path = '/content/gdrive/My Drive/datasets/originals'

def loadImages(path, subfolder_path):
  image_files = sorted([os.path.join(path, subfolder_path, file) for file in os.listdir(path + '/' + subfolder_path) if file.endswith('.bmp')])
  return image_files

def displayImage(img, title = "Originals"):
  plt.imshow(img, cmap='gray',)
  plt.title(title)
  plt.show()

def resizeImage(width, height, img):
  dim = (width, height)
  return cv2.resize(img, dim, interpolation=cv2.INTER_LINEAR)

def getImgShape(img):
  try:
    return img.shape
  except AttributeError:
    return "Shape not found"

# m -> malignant
# b -> benign

m_path_dataset = loadImages(data_drive_path, 'malignant')
b_path_dataset = loadImages(data_drive_path, 'benign')

m_path_dataset[0]

m_img_ds = [cv2.imread(i, cv2.IMREAD_GRAYSCALE) for i in m_path_dataset]
b_img_ds = [cv2.imread(i, cv2.IMREAD_GRAYSCALE) for i in b_path_dataset]

m_img_ds[0]

getImgShape(m_img_ds[0])

getImgShape(b_img_ds[0])

processed_m_img_ds = [resizeImage(95, 75, i) for i in m_img_ds]
processed_b_img_ds = [resizeImage(95, 75, i) for i in b_img_ds]

processed_m_img_ds[0]

getImgShape(processed_m_img_ds[0])

displayImage(processed_m_img_ds[0], 'Malignant')

displayImage(b_img_ds[0], 'Benign')

m_target = np.zeros((len(processed_m_img_ds), 1), dtype=int)

m_target.shape

m_target[0]

b_target = np.ones((len(b_img_ds), 1), dtype=int)

b_target.shape

b_target[0]

m_b_target_ds = np.concatenate((m_target, b_target), axis=0)

m_b_target_ds.shape

# combine the both dataset

m_b_img_ds = np.concatenate((processed_m_img_ds, processed_b_img_ds), axis=0)

displayImage(m_b_img_ds[0])

m_b_img_ds.shape

displayImage(m_b_img_ds[150])

len(m_b_img_ds)

# shuffle the dataset

img_ds = list()
target_ds = list()

m_b_img_ds = list(m_b_img_ds)
m_b_target_ds = list(m_b_target_ds)

for i in range(len(m_b_img_ds)):
  index = random.choice(range(len(m_b_img_ds)))

  img_ds.append(m_b_img_ds[index])
  target_ds.append(m_b_target_ds[index])

  m_b_img_ds.pop(index)
  m_b_target_ds.pop(index)

img_ds = np.array(img_ds)
target_ds = np.array(target_ds)

print(img_ds.shape, target_ds.shape)

img_ds_reshaped = img_ds.reshape(img_ds.shape[0], -1) 

np.savetxt("mammographic_images_mat.txt", img_ds_reshaped)

files.download('mammographic_images_mat.txt')

# target_ds_reshaped = target_ds.reshape(target_ds.shape[0], -1) 

np.savetxt("mammographic_images_mat_y.txt", target_ds)

files.download('mammographic_images_mat_y.txt')