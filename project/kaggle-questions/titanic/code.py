import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load data
x_train = pd.read_csv('train.csv')
y_train = x_train['Survived'].values  # 1D array for sklearn

# Fill missing values
x_train['Age'] = x_train['Age'].fillna(x_train['Age'].median())
x_train['Fare'] = x_train['Fare'].fillna(x_train['Fare'].median())

# Drop unused columns
x_train = x_train.drop(['Survived', 'PassengerId', 'Cabin', 'Name', 'Ticket'], axis=1)

# Define categorical and numerical features
categorical_features = ['Sex', 'Embarked']
numerical_features = ['Age', 'Pclass', 'SibSp', 'Parch', 'Fare']
oe=OneHotEncoder()
sc=StandardScaler()

# Create ColumnTransformer to handle preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', oe, categorical_features),
        ('num', sc, numerical_features)
    ])

# Fit and transform training data
x_train_processed = preprocessor.fit_transform(x_train)

# Create and train SVR model
svr = SVR()
svr.fit(x_train_processed, y_train)

# Prepare test data similarly
x_test = pd.read_csv('test.csv')
x_test['Age'] = x_test['Age'].fillna(x_test['Age'].median())
x_test['Fare'] = x_test['Fare'].fillna(x_test['Fare'].median())
x_test = x_test.drop(['PassengerId', 'Cabin', 'Name', 'Ticket'], axis=1)

# Transform test data using the same preprocessor (don't fit again!)
x_test_processed = preprocessor.transform(x_test)

# Predict
predictions = svr.predict(x_test_processed)
plt.scatter(range(len(y_train)),y_train)
plt.scatter(range(len(x_test_processed)),predictions)

model2=LinearRegression()
model2.fit(x_train_processed, y_train)
predictions = model2.predict(x_test_processed)
plt.scatter(range(len(y_train)),y_train,color='red')
plt.scatter(range(len(x_test_processed)),predictions,marker='x')
plt.show()


print(predictions)







