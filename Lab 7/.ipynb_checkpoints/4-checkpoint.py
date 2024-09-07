import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import os

# Set the path to your dataset
data_dir = 'Collage_python\Lab 7\flowers'  # Change this to the path of your dataset

# Image dimensions
img_height, img_width = 128, 128
batch_size = 32

# Data augmentation and preprocessing
datagen = ImageDataGenerator(
    rescale=1.0/255.0,  # Rescale pixel values
    validation_split=0.2  # Split 20% for validation
)

# Load training data
train_data = datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'
)

# Load validation data
validation_data = datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'
)

# Define the MLP model
model = Sequential([
    Flatten(input_shape=(img_height, img_width, 3)),  # Flatten the input images
    Dense(128, activation='relu'),  # Fully connected layer with 128 units
    Dropout(0.5),  # Dropout for regularization
    Dense(64, activation='relu'),  # Another fully connected layer
    Dense(train_data.num_classes, activation='softmax')  # Output layer with softmax activation
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Display the model architecture
model.summary()

# Train the model
history = model.fit(
    train_data,
    validation_data=validation_data,
    epochs=20,  # You can increase epochs based on performance
    verbose=1
)

# Evaluate the model
loss, accuracy = model.evaluate(validation_data)
print(f'Validation Loss: {loss:.4f}')
print(f'Validation Accuracy: {accuracy:.4f}')

# Plot training & validation accuracy
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.title('Model Accuracy')
plt.show()

# Plot training & validation loss
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.title('Model Loss')
plt.show()
