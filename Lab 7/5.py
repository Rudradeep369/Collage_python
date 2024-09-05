from sklearn.svm import SVC
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load Data
X, y = fetch_openml('mnist_784', version=1, return_X_y=True)
X /= 255.0  # Normalize

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# SVM Model
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
predictions = svm.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))
