#!/usr/bin/env python
# coding: utf-8

# In[24]:


import cv2
import numpy as np
import os

def augment_image(img):
    # Choose a random number between 0 and 3 to decide the type of augmentation
    num = np.random.randint(0, 4)
    
    if num == 0:
        # Rotate the image
        angle = np.random.uniform(-45, 45)
        M = cv2.getRotationMatrix2D((img.shape[1] / 2, img.shape[0] / 2), angle, 1)
        img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    elif num == 1:
        # Flip the image horizontally
        img = cv2.flip(img, 1)
    elif num == 2:
        # Change the color channel of the image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        # Add Gaussian noise to the image
        mean = 0
        var = 0.1
        sigma = var**0.5
        gaussian = np.random.normal(mean, sigma, img.shape)
        img = img + gaussian
        img = np.clip(img, 0, 255)
    return img

# Path to the folder containing the images
folder_path = 'F:/Ortho_Data/Annotation_Images/Barely_Casselton/selected_images_07012022_casselton_barley_P1_200ft_transparent_mosaic_group1/'

# List all the images in the folder
images = [img for img in os.listdir(folder_path) if img.endswith('.jpg')]

# Number of images to augment
num_augment = int(len(images) / 2)

# Choose random images from the list to augment
augment_indices = np.random.choice(len(images), num_augment, replace=False)

selected_images = [images[i] for i in augment_indices]
for i, img_name in enumerate(selected_images):
    # Load the image
    img = cv2.imread(os.path.join(folder_path, img_name))
    img = augment_image(img)
        
    # Save the augmented image
    cv2.imwrite(os.path.join(folder_path, 'augmented_' + img_name), img)


# In[6]:


folder_path = 'F:/Ortho_Data/Annotation_Images/Barely_Casselton/selected_images_Cass_Barley_Autel6K_100ft_06072021_transparent_mosaic_group1/'


# In[7]:


images = [img for img in os.listdir(folder_path) if img.endswith('.jpg')]
print(images)


# In[9]:


num_augment = int(len(images) / 2)
print(num_augment)


# In[11]:


augment_indices = np.random.choice(len(images), num_augment, replace=False)
print(augment_indices)


# In[16]:


print(len(augment_indices))


# In[18]:


selected_images = [images[i] for i in augment_indices]
print(selected_images)


# In[19]:


print(len(selected_images))


# In[ ]:




