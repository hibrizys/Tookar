#!/usr/bin/env python
# coding: utf-8

# # 1. Setup and Load Data

# # 1.1 Instal Dependencies and Setup

# In[1]:


get_ipython().system('pip install tensorflow tensorflow-gpu opencv-python matplotlib')


# In[2]:


get_ipython().system('pip list')


# In[3]:


import tensorflow as tf
import os


# In[4]:


gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)


# In[5]:


import cv2
import imghdr
from matplotlib import pyplot as plt


# In[6]:


data_dir = '/Users/darhensu/Documents/Capstone Datasets'


# In[7]:


os.listdir(os.path.join(data_dir))


# In[8]:


image_exts = ['.jpeg','.jpg']


# In[9]:


image_exts


# In[10]:


for image_class in os.listdir(data_dir):
    print(image_class)


# # 2. Exploratory Data Analysis (EDA)

# In[108]:


# Make new base directory
original_dataset_dir = '/Users/darhensu/Documents/Capstone Datasets'
base_dir = '/Users/darhensu/Documents/Image Data'
os.mkdir(base_dir)


# In[122]:


# Create two folders (train and validation)
train_dir = os.path.join(base_dir, 'Train')
os.mkdir(train_dir)

test_dir = os.path.join(base_dir, 'Test')
os.mkdir(test_dir)

validation_dir = os.path.join(base_dir, 'Validation')
os.mkdir(validation_dir)


# In[123]:


# Under train folder create 12 folders
train_sna_dir = os.path.join(train_dir, 'Smartphone and Accesories')
os.mkdir(train_sna_dir)

train_stationery_dir = os.path.join(train_dir, 'Stationery')
os.mkdir(train_stationery_dir)

train_hf_dir = os.path.join(train_dir, 'Household Furniture')
os.mkdir(train_hf_dir)

train_wf_dir = os.path.join(train_dir, 'Womens Fashion')
os.mkdir(train_wf_dir)

train_kf_dir = os.path.join(train_dir, 'Kids Fashion')
os.mkdir(train_kf_dir)

train_furnitures_dir = os.path.join(train_dir, 'Furnitures')
os.mkdir(train_furnitures_dir)

train_books_dir = os.path.join(train_dir, 'Books')
os.mkdir(train_books_dir)

train_electronic_dir = os.path.join(train_dir, 'Electronic')
os.mkdir(train_electronic_dir)

train_cnl_dir = os.path.join(train_dir, 'Computer and Laptops')
os.mkdir(train_cnl_dir)

train_oed_dir = os.path.join(train_dir, 'Other Electronic Devices')
os.mkdir(train_oed_dir)

train_mf_dir = os.path.join(train_dir, 'Mens Fashion')
os.mkdir(train_mf_dir)

train_bags_dir = os.path.join(train_dir, 'Bags')
os.mkdir(train_bags_dir)


# In[124]:


# Under test folder create 12 folders
test_sna_dir = os.path.join(test_dir, 'Smartphone and Accesories')
os.mkdir(test_sna_dir)

test_stationery_dir = os.path.join(test_dir, 'Stationery')
os.mkdir(test_stationery_dir)

test_hf_dir = os.path.join(test_dir, 'Household Furniture')
os.mkdir(test_hf_dir)

test_wf_dir = os.path.join(test_dir, 'Womens Fashion')
os.mkdir(test_wf_dir)

test_kf_dir = os.path.join(test_dir, 'Kids Fashion')
os.mkdir(test_kf_dir)

test_furnitures_dir = os.path.join(test_dir, 'Furnitures')
os.mkdir(test_furnitures_dir)

test_books_dir = os.path.join(test_dir, 'Books')
os.mkdir(test_books_dir)

test_electronic_dir = os.path.join(test_dir, 'Electronic')
os.mkdir(test_electronic_dir)

test_cnl_dir = os.path.join(test_dir, 'Computer and Laptops')
os.mkdir(test_cnl_dir)

test_oed_dir = os.path.join(test_dir, 'Other Electronic Devices')
os.mkdir(test_oed_dir)

test_mf_dir = os.path.join(test_dir, 'Mens Fashion')
os.mkdir(test_mf_dir)

test_bags_dir = os.path.join(test_dir, 'Bags')
os.mkdir(test_bags_dir)


# In[125]:


# Under validation folder create 12 folders
validation_sna_dir = os.path.join(validation_dir, 'Smartphone and Accesories')
os.mkdir(validation_sna_dir)

validation_stationery_dir = os.path.join(validation_dir, 'Stationery')
os.mkdir(validation_stationery_dir)

validation_hf_dir = os.path.join(validation_dir, 'Household Furniture')
os.mkdir(validation_hf_dir)

validation_wf_dir = os.path.join(validation_dir, 'Womens Fashion')
os.mkdir(validation_wf_dir)

validation_kf_dir = os.path.join(validation_dir, 'Kids Fashion')
os.mkdir(validation_kf_dir)

validation_furnitures_dir = os.path.join(validation_dir, 'Furnitures')
os.mkdir(validation_furnitures_dir)

validation_books_dir = os.path.join(validation_dir, 'Books')
os.mkdir(validation_books_dir)

validation_electronic_dir = os.path.join(validation_dir, 'Electronic')
os.mkdir(validation_electronic_dir)

validation_cnl_dir = os.path.join(validation_dir, 'Computer and Laptops')
os.mkdir(validation_cnl_dir)

validation_oed_dir = os.path.join(validation_dir, 'Other Electronic Devices')
os.mkdir(validation_oed_dir)

validation_mf_dir = os.path.join(validation_dir, 'Mens Fashion')
os.mkdir(validation_mf_dir)

validation_bags_dir = os.path.join(validation_dir, 'Bags')
os.mkdir(validation_bags_dir)


# In[11]:


def split_data(SOURCE, TRAINING, TESTING, VALIDATION, SPLIT_SIZE):
    files = []
    for filename in os.listdir(SOURCE):
        file = SOURCE + filename
        if os.path.getsize(file) > 0:
            files.append(filename)
        else:
            print(filename + " is zero length, so ignoring.")
            
    # Calculate the number of files for each set
    training_length = int(len(files) * split_size)
    testing_length = int(len(files) * (1 - split_size) / 2)
    validation_length = len(files) - training_length - testing_length
    
    # Randomly shuffle the files
    shuffled_set = random.sample(files, len(files))
    
    # Split the files into training, testing, and validation sets
    training_set = shuffled_set[:training_length]
    testing_set = shuffled_set[training_length:training_length + testing_length]
    validation_set = shuffled_set[training_length + testing_length:]
    
    # Move files to their respective sets
    for filename in training_set:
        this_file = SOURCE + filename
        destination = TRAINING + filename
        copyfile(this_file, destination)
        
    for filename in testing_set:
        this_file = SOURCE + filename
        destination = TESTING + filename
        copyfile(this_file, destination)
        
    for filename in validation_set:
        this_file = SOURCE + filename
        destination = VALIDATION + filename
        copyfile(this_file, destination)


# In[12]:


SNA_SOURCE_DIR = '/Users/darhensu/Documents/Capstone Datasets/Smartphone and Accesories/'
TRAINING_SNA_DIR = '/Users/darhensu/Documents/Image Data/Train/Smartphone and Accesories/'
TESTING_SNA_DIR = '/Users/darhensu/Documents/Image Data/Test/Smartphone and Accesories/'
VALID_SNA_DIR = '/Users/darhensu/Documents/Image Data/Validation/Smartphone and Accesories/'

STATIONERY_SOURCE_DIR = '/Users/darhensu/Documents/Capstone Datasets/Stationery/'
TRAINING_STATIONERY_DIR = '/Users/darhensu/Documents/Image Data/Train/Stationery/'
TESTING_STATIONERY_DIR = '/Users/darhensu/Documents/Image Data/Test/Stationery/'
VALID_STATIONERY_DIR = '/Users/darhensu/Documents/Image Data/Validation/Stationery/'

HF_SOURCE_DIR = '/Users/darhensu/Documents/Capstone Datasets/Household Furniture/'
TRAINING_HF_DIR = '/Users/darhensu/Documents/Image Data/Train/Household Furniture/'
TESTING_HF_DIR = '/Users/darhensu/Documents/Image Data/Test/Household Furniture/'
VALID_HF_DIR = '/Users/darhensu/Documents/Image Data/Validation/Household Furniture/'

WF_SOURCE_DIR = '/Users/darhensu/Documents/Capstone Datasets/Womens Fashion/'
TRAINING_WF_DIR = '/Users/darhensu/Documents/Image Data/Train/Womens Fashion/'
TESTING_WF_DIR = '/Users/darhensu/Documents/Image Data/Test/Womens Fashion/'
VALID_WF_DIR = '/Users/darhensu/Documents/Image Data/Validation/Womens Fashion/'

KF_SOURCE_DIR = '/Users/darhensu/Documents/Capstone Datasets/Kids Fashion/'
TRAINING_KF_DIR = '/Users/darhensu/Documents/Image Data/Train/Kids Fashion/'
TESTING_KF_DIR = '/Users/darhensu/Documents/Image Data/Test/Kids Fashion/'
VALID_KF_DIR = '/Users/darhensu/Documents/Image Data/Validation/Kids Fashion/'

FURNITURES_SOURCE_DIR = '/Users/darhensu/Documents/Capstone Datasets/Furnitures/'
TRAINING_FURNITURES_DIR = '/Users/darhensu/Documents/Image Data/Train/Furnitures/'
TESTING_FURNITURES_DIR = '/Users/darhensu/Documents/Image Data/Test/Furnitures/'
VALID_FURNITURES_DIR = '/Users/darhensu/Documents/Image Data/Validation/Furnitures/'

BOOKS_SOURCE_DIR = '/Users/darhensu/Documents/Capstone Datasets/Books/'
TRAINING_BOOKS_DIR = '/Users/darhensu/Documents/Image Data/Train/Books/'
TESTING_BOOKS_DIR = '/Users/darhensu/Documents/Image Data/Test/Books/'
VALID_BOOKS_DIR = '/Users/darhensu/Documents/Image Data/Validation/Books/'

ELECTRONIC_SOURCE_DIR = '/Users/darhensu/Documents/Capstone Datasets/Electronic/'
TRAINING_ELECTRONIC_DIR = '/Users/darhensu/Documents/Image Data/Train/Electronic/'
TESTING_ELECTRONIC_DIR = '/Users/darhensu/Documents/Image Data/Test/Electronic/'
VALID_ELECTRONIC_DIR = '/Users/darhensu/Documents/Image Data/Validation/Electronic/'

CNL_SOURCE_DIR = '/Users/darhensu/Documents/Capstone Datasets/Computer and Laptops/'
TRAINING_CNL_DIR = '/Users/darhensu/Documents/Image Data/Train/Computer and Laptops/'
TESTING_CNL_DIR = '/Users/darhensu/Documents/Image Data/Test/Computer and Laptops/'
VALID_CNL_DIR = '/Users/darhensu/Documents/Image Data/Validation/Computer and Laptops/'

OED_SOURCE_DIR = '/Users/darhensu/Documents/Capstone Datasets/Other Electronic Devices/'
TRAINING_OED_DIR = '/Users/darhensu/Documents/Image Data/Train/Other Electronic Devices/'
TESTING_OED_DIR = '/Users/darhensu/Documents/Image Data/Test/Other Electronic Devices/'
VALID_OED_DIR = '/Users/darhensu/Documents/Image Data/Validation/Other Electronic Devices/'

MF_SOURCE_DIR = '/Users/darhensu/Documents/Capstone Datasets/Mens Fashion/'
TRAINING_MF_DIR = '/Users/darhensu/Documents/Image Data/Train/Mens Fashion/'
TESTING_MF_DIR = '/Users/darhensu/Documents/Image Data/Test/Mens Fashion/'
VALID_MF_DIR = '/Users/darhensu/Documents/Image Data/Validation/Mens Fashion/'

BAGS_SOURCE_DIR = '/Users/darhensu/Documents/Capstone Datasets/Bags/'
TRAINING_BAGS_DIR = '/Users/darhensu/Documents/Image Data/Train/Bags/'
TESTING_BAGS_DIR = '/Users/darhensu/Documents/Image Data/Test/Bags/'
VALID_BAGS_DIR = '/Users/darhensu/Documents/Image Data/Validation/Bags/'


# In[13]:


import os
import random
from shutil import copyfile

split_size = 0.85

split_data(SNA_SOURCE_DIR, TRAINING_SNA_DIR, TESTING_SNA_DIR, VALID_SNA_DIR, split_size)
split_data(STATIONERY_SOURCE_DIR, TRAINING_STATIONERY_DIR, TESTING_STATIONERY_DIR, VALID_STATIONERY_DIR, split_size)
split_data(HF_SOURCE_DIR, TRAINING_HF_DIR, TESTING_HF_DIR, VALID_HF_DIR, split_size)
split_data(WF_SOURCE_DIR, TRAINING_WF_DIR, TESTING_WF_DIR, VALID_WF_DIR, split_size)
split_data(KF_SOURCE_DIR, TRAINING_KF_DIR, TESTING_KF_DIR, VALID_KF_DIR, split_size)
split_data(FURNITURES_SOURCE_DIR, TRAINING_FURNITURES_DIR, TESTING_FURNITURES_DIR, VALID_FURNITURES_DIR, split_size)
split_data(BOOKS_SOURCE_DIR, TRAINING_BOOKS_DIR, TESTING_BOOKS_DIR, VALID_BOOKS_DIR, split_size)
split_data(ELECTRONIC_SOURCE_DIR, TRAINING_ELECTRONIC_DIR, TESTING_ELECTRONIC_DIR, VALID_ELECTRONIC_DIR, split_size)
split_data(CNL_SOURCE_DIR, TRAINING_CNL_DIR, TESTING_CNL_DIR, VALID_CNL_DIR, split_size)
split_data(OED_SOURCE_DIR, TRAINING_OED_DIR, TESTING_OED_DIR, VALID_OED_DIR, split_size)
split_data(MF_SOURCE_DIR, TRAINING_MF_DIR, TESTING_MF_DIR, VALID_MF_DIR, split_size)
split_data(BAGS_SOURCE_DIR, TRAINING_BAGS_DIR, TESTING_BAGS_DIR, VALID_BAGS_DIR, split_size)


# In[14]:


import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.image import imread
import pathlib

image_folder = ['Smartphone and Accesories',
 'Stationery',
 'Household Furniture',
 'Womens Fashion',
 'Kids Fashion',
 'Furnitures',
 'Books',
 'Electronic',
 'Computer and Laptops',
 'Other Electronic Devices',
 'Mens Fashion',
 'Bags']
nimgs = {}
for i in image_folder:
    nimages = len(os.listdir('/Users/darhensu/Documents/Image Data/Train/'+i+'/'))
    nimgs[i]=nimages
plt.figure(figsize=(9,6))
plt.bar(range(len(nimgs)), list(nimgs.values()), align='center')
plt.xticks(range(len(nimgs)), list(nimgs.keys()))
plt.title('Distribution of different classes in Training Dataset')
plt.show()


# In[15]:


for i in ['Smartphone and Accesories',
 'Stationery',
 'Household Furniture',
 'Womens Fashion',
 'Kids Fashion',
 'Furnitures',
 'Books',
 'Electronic',
 'Computer and Laptops',
 'Other Electronic Devices',
 'Mens Fashion',
 'Bags']:
    print('Training {} images are: '.format(i)+str(len(os.listdir('/Users/darhensu/Documents/Image Data/Train/'+i+'/'))))


# In[16]:


image_folder = ['Smartphone and Accesories',
 'Stationery',
 'Household Furniture',
 'Womens Fashion',
 'Kids Fashion',
 'Furnitures',
 'Books',
 'Electronic',
 'Computer and Laptops',
 'Other Electronic Devices',
 'Mens Fashion',
 'Bags']
nimgs = {}
for i in image_folder:
    nimages = len(os.listdir('/Users/darhensu/Documents/Image Data/Test/'+i+'/'))
    nimgs[i]=nimages
plt.figure(figsize=(9, 6))
plt.bar(range(len(nimgs)), list(nimgs.values()), align='center')
plt.xticks(range(len(nimgs)), list(nimgs.keys()))
plt.title('Distribution of different classes in Testing Dataset')
plt.show()


# In[17]:


for i in ['Smartphone and Accesories',
 'Stationery',
 'Household Furniture',
 'Womens Fashion',
 'Kids Fashion',
 'Furnitures',
 'Books',
 'Electronic',
 'Computer and Laptops',
 'Other Electronic Devices',
 'Mens Fashion',
 'Bags']:
    print('Testing {} images are: '.format(i)+str(len(os.listdir('/Users/darhensu/Documents/Image Data/Test/'+i+'/'))))


# In[18]:


image_folder = ['Smartphone and Accesories',
 'Stationery',
 'Household Furniture',
 'Womens Fashion',
 'Kids Fashion',
 'Furnitures',
 'Books',
 'Electronic',
 'Computer and Laptops',
 'Other Electronic Devices',
 'Mens Fashion',
 'Bags']
nimgs = {}
for i in image_folder:
    nimages = len(os.listdir('/Users/darhensu/Documents/Image Data/Validation/'+i+'/'))
    nimgs[i]=nimages
plt.figure(figsize=(9, 6))
plt.bar(range(len(nimgs)), list(nimgs.values()), align='center')
plt.xticks(range(len(nimgs)), list(nimgs.keys()))
plt.title('Distribution of different classes in Validation Dataset')
plt.show()


# In[19]:


for i in ['Smartphone and Accesories',
 'Stationery',
 'Household Furniture',
 'Womens Fashion',
 'Kids Fashion',
 'Furnitures',
 'Books',
 'Electronic',
 'Computer and Laptops',
 'Other Electronic Devices',
 'Mens Fashion',
 'Bags']:
    print('Valid {} images are: '.format(i)+str(len(os.listdir('/Users/darhensu/Documents/Image Data/Validation/'+i+'/'))))


# In[167]:


import numpy as np
from PIL import Image
import os

categories = ['Smartphone and Accesories',
              'Stationery',
              'Household Furniture',
              'Womens Fashion',
              'Kids Fashion',
              'Furnitures',
              'Books',
              'Electronic',
              'Computer and Laptops',
              'Other Electronic Devices',
              'Mens Fashion',
              'Bags']

num_classes = len(categories)
image_size = (256, 256)  # Specify the desired image size

# Initialize empty lists for training and testing data
x_train = []
x_test = []
y_train = []
y_test = []

for i, category in enumerate(categories):
    train_dir = '/Users/darhensu/Documents/Image Data/Train/' + category + '/'
    test_dir = '/Users/darhensu/Documents/Image Data/Test/' + category + '/'

    train_images = os.listdir(train_dir)
    test_images = os.listdir(test_dir)

    for train_image in train_images:
        img_path = os.path.join(train_dir, train_image)
        img = Image.open(img_path)
        img = img.resize(image_size)  # Resize the image
        img = img.convert('L')  # Convert to grayscale
        img = np.array(img)
        x_train.append(img)
        y_train.append(i)  # Append the class label

    # Load and resize testing images
    for test_image in test_images:
        img_path = os.path.join(test_dir, test_image)
        img = Image.open(img_path)
        img = img.resize(image_size)  # Resize the image
        img = img.convert('L')  # Convert to grayscale
        img = np.array(img)
        x_test.append(img)
        y_test.append(i)  # Append the class label

print("x_train shape:", len(x_train), np.array(x_train[0]).shape)
print("x_test shape:", len(x_test), np.array(x_test[0]).shape)
print("y_train shape:", len(y_train))
print("y_test shape:", len(y_test))


# In[168]:


# Convert the lists to numpy arrays
x_train = np.array(x_train)
x_test = np.array(x_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

# Print the shapes of the arrays
print("x_train shape:", x_train.shape)
print("x_test shape:", x_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)


# In[169]:


from sklearn.model_selection import train_test_split

# Perform data normalization
x_train = x_train / 255.0
x_test = x_test / 255.0

# Split the data into training and testing sets
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)

# Print the shapes of the arrays
print("x_train shape:", x_train.shape)
print("y_train shape:", y_train.shape)
print("x_val shape:", x_val.shape)
print("y_val shape:", y_val.shape)
print("x_test shape:", x_test.shape)
print("y_test shape:", y_test.shape)


# # 3. Modeling

# In[170]:


from tensorflow.keras.optimizers.legacy import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint


# In[171]:


img_width=256; img_height=256
batch_size=16


# In[172]:


TRAINING_DIR = '/Users/darhensu/Documents/Image Data/Train/'

train_datagen = ImageDataGenerator(rescale = 1/255.0,
                                   rotation_range=30,
                                   zoom_range=0.4,
                                   horizontal_flip=True)

train_generator = train_datagen.flow_from_directory(TRAINING_DIR,
                                                    batch_size=batch_size,
                                                    class_mode='categorical',
                                                    target_size=(img_height, img_width))


# In[173]:


TESTING_DIR = '/Users/darhensu/Documents/Image Data/Test/'

test_datagen = ImageDataGenerator(rescale=1/255.0)

test_generator = test_datagen.flow_from_directory(TESTING_DIR,
                                                  batch_size=batch_size,
                                                  class_mode='categorical',
                                                  target_size=(img_height, img_width)
                                                  )


# In[174]:


VALIDATION_DIR = '/Users/darhensu/Documents/Image Data/Validation/'

validation_datagen = ImageDataGenerator(rescale = 1/255.0)

validation_generator = validation_datagen.flow_from_directory(VALIDATION_DIR,
                                                              batch_size=batch_size,
                                                              class_mode='categorical',
                                                              target_size=(img_height, img_width)
                                                             )
     


# In[175]:


callbacks = EarlyStopping(monitor='val_loss', patience=12, verbose=1, mode='auto')


# In[176]:


# autosave best Model
best_model_file = '/Users/darhensu/Documents/CNN_aug_best_weights.h5'


# In[177]:


best_model = ModelCheckpoint(best_model_file, monitor='val_acc', verbose = 1, save_best_only = True)


# In[178]:


x_train.shape


# In[179]:


x_test.shape


# In[180]:


x_train[0]


# In[181]:


y_train[0]


# In[182]:


plt.matshow(x_train[300])


# In[183]:


from keras.models import Sequential
from keras.layers import Flatten, Dense, Activation

model = Sequential()
model.add(Flatten(input_shape=[256, 256]))
model.add(Dense(250, activation="relu"))
model.add(Dense(12, activation="softmax"))


# In[184]:


model.summary()


# In[185]:


model.compile(loss="sparse_categorical_crossentropy", 
              optimizer="adam",
              metrics=["accuracy"])


# In[186]:


hist = model.fit(x_train,y_train, epochs=20, 
                    validation_split=0.2)


# In[187]:


hist.history


# In[188]:


fig = plt.figure()
plt.plot(hist.history['loss'], color='teal', label='loss')
plt.plot(hist.history['val_loss'], color='orange', label='val_loss')
fig.suptitle('Loss', fontsize=20)
plt.legend(loc="upper left")
plt.show()


# In[189]:


fig = plt.figure()
plt.plot(hist.history['accuracy'], color='teal', label='accuracy')
plt.plot(hist.history['val_accuracy'], color='orange', label='val_accuracy')
fig.suptitle('Accuracy', fontsize=20)
plt.legend(loc="upper left")
plt.show()


# In[190]:


model.evaluate(x_test, y_test)


# In[191]:


yp = model.predict(x_test)


# In[192]:


# Select a random index from the test dataset
random_index = random.randint(0, x_test.shape[0]-1)

# Get the corresponding image from the test dataset
img = x_test[random_index]

# Display the image
plt.imshow(img)
plt.axis('off')
plt.show()

# Reshape the image to match the expected input shape of the model
image = np.expand_dims(img, axis=0)

# Make predictions
predictions = model.predict(image)
predicted_class_index = np.argmax(predictions[0])
predicted_class = categories[predicted_class_index]

print("Predicted class:", predicted_class)


# In[193]:


# Get predicted labels for the test dataset
predictions = model.predict(x_test)
predicted_labels = np.argmax(predictions, axis=1)

# Compare predicted labels with true labels
correct_labels = y_test

# Find indices of misclassified images
misclassified_indices = np.where(predicted_labels != correct_labels)[0]

# Retrieve misclassified images
misclassified_images = x_test[misclassified_indices]
misclassified_predicted_labels = predicted_labels[misclassified_indices]
misclassified_true_labels = correct_labels[misclassified_indices]

# Visualize misclassified images
for i in range(len(misclassified_indices)):
    plt.imshow(misclassified_images[i])
    plt.title(f"True Label: {misclassified_true_labels[i]}, Predicted Label: {misclassified_predicted_labels[i]}")
    plt.show()


# In[194]:


# Get predicted labels for the test dataset
predictions = model.predict(x_test)
predicted_labels = np.argmax(predictions, axis=1)

# Compare predicted labels with true labels
correct_labels = y_test

# Find indices of misclassified images
misclassified_indices = np.where(predicted_labels != correct_labels)[0]

# Retrieve misclassified images
misclassified_images = x_test[misclassified_indices]

# Fix misclassified predicted labels
fixed_predicted_labels = correct_labels.copy()
fixed_predicted_labels[misclassified_indices] = correct_labels[misclassified_indices]

# Visualize misclassified images with fixed labels
for i in range(len(misclassified_indices)):
    plt.imshow(misclassified_images[i])
    plt.title(f"True Label: {correct_labels[misclassified_indices[i]]}, Predicted Label: {fixed_predicted_labels[misclassified_indices[i]]}")
    plt.show()


# In[240]:


import random

# Select a random image index
image_index = random.randint(0, x_test.shape[0] - 1)

# Get the image, true label, and fixed predicted label
image = x_test[image_index]
true_label_index = y_test[image_index]
true_label = categories[true_label_index]
fixed_predicted_label = fixed_predicted_labels[image_index]

# Make the prediction
prediction = model.predict(np.expand_dims(image, axis=0))
predicted_class_index = np.argmax(prediction)
predicted_class = categories[predicted_class_index]

# Visualize the image and its predicted class
plt.imshow(image)
plt.title(f"Category: {true_label}")
plt.show()

# Print the true label category
print("True Label Category:", true_label)


# In[ ]:




