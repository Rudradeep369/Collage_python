import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

# Step 2: Load the Iris Dataset
iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['target'] = iris.target

# Step 3: Summarize the Dataset
# Check dimensions
print("Dataset Dimensions:", data.shape)

# Peek at the data
print("\nFirst 5 Rows of the Dataset:")
print(data.head())

# Statistical summary of all attributes
print("\nStatistical Summary:")
print(data.describe())

# Breakdown of the data by class variable
print("\nClass Distribution:")
print(data['target'].value_counts())

# Step 4: Visualize the Dataset
# Univariate Plots (Histograms)
data.hist(figsize=(10, 8))
plt.suptitle('Histogram of Each Feature')
plt.show()

# Multivariate Plots (Pairplot)
sns.pairplot(data, hue='target', markers=["o", "s", "D"])
plt.suptitle('Pairplot of Features', y=1.02)
plt.show()

# Step 5: Evaluate Algorithms
# Separate the dataset into input features (X) and target variable (y)
X = data.drop('target', axis=1)
y = data['target']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Set up 10-fold cross-validation
kfold = KFold(n_splits=10, random_state=42, shuffle=True)

# Define the models to test
models = {
    'Logistic Regression (LR)': LogisticRegression(max_iter=200),
    'Linear Discriminant Analysis (LDA)': LinearDiscriminantAnalysis(),
    'K-Nearest Neighbors (KNN)': KNeighborsClassifier(),
    'Classification and Regression Trees (CART)': DecisionTreeClassifier(),
    'Gaussian Naive Bayes (NB)': GaussianNB(),
    'Support Vector Machines (SVM)': SVC()
}

# Evaluate each model
results = {}
print("\nCross-Validation Results:")
for name, model in models.items():
    cv_results = cross_val_score(model, X_train, y_train, cv=kfold, scoring='accuracy')
    results[name] = cv_results.mean()
    print(f"{name}: {cv_results.mean():.4f}")

# Step 6: Make Predictions
# Select the best model based on cross-validation results
best_model_name = max(results, key=results.get)
best_model = models[best_model_name]
print(f"\nBest Model: {best_model_name}")

# Train the best model on the training set
best_model.fit(X_train, y_train)

# Make predictions on the test set
predictions = best_model.predict(X_test)

# Evaluate the predictions
print("\nAccuracy Score on Test Set:")
print(accuracy_score(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))
