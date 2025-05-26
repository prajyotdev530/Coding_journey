import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.model_selection import train_test_split

dataset=pd.read_csv('/Users/prajyotmore/Downloads/study_material/Machine-Learning-A-Z-Codes-Datasets/Part 7 - Natural Language Processing/Section 36 - Natural Language Processing/Python/Restaurant_Reviews.tsv',delimiter='\t',quoting=3)
Y=dataset.iloc[:,-1].values
corpus=[]
for i in range(0,1000):
    review=re.sub('[^a-zA-Z]',' ',dataset.iloc[i,0])
    review=review.lower()
    review=review.split()
    pd=PorterStemmer()
    review=[pd.stem(word)for word in review if word not in set(stopwords.words('english'))]
    review=' '.join(review)
    review=review.lower()
    corpus.append(review)

print(np.array(corpus).reshape(-1,1))
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
X=cv.fit_transform(corpus).toarray()
print(X)
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=2)
from sklearn.naive_bayes import MultinomialNB
model=MultinomialNB()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print(y_pred)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print(cm)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pred))
new_review = 'I hate this restaurant so much'
new_review=re.sub('[^a-zA-Z]',' ',new_review)
new_review=new_review.lower()
new_review=new_review.split()
porter = PorterStemmer()
new_review=[porter.stem(word)for word in new_review if word not in set(stopwords.words('english'))]
new_review=' '.join(new_review)
new_review=new_review.lower()
new_corpus=[new_review]
new_x_test=cv.transform(new_corpus).toarray()
new_y_pred=model.predict(new_x_test)
print(new_y_pred)




