from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cross_validation import train_test_split
from sklearn import svm
from sklearn.metrics import classification_report
import sys
import os
import time

'''
importing data
'''
data = []
data_labels = []
with open('./pos.txt') as f:
    for i in f:
        data.append(i)
        data_labels.append('pos')
with open('./neg.txt') as f:
    for i in f:
        data.append(i)
        data_labels.append('neg')
with open ('./neutr.txt') as f:
    for i in f:
        data.append(i)
        data_labels.append('neutr')
        
'''
splitting data into train and test set
        
'''
X_train, X_test, y_train, y_test  = train_test_split(
        data, 
        data_labels,
        train_size=0.80, 
        random_state=1234)
        

'''
creating tf-idf scheme
'''
vectorizer = TfidfVectorizer(min_df=5,
                                 max_df = 0.8,
                                 sublinear_tf=True,
                                 use_idf=True)
    train_vectors = vectorizer.fit_transform(X_train)
    test_vectors = vectorizer.transform(X_test)

'''
training classifier
'''
classifier_rbf = svm.SVC()
    classifier_rbf.fit(train_vectors, train_labels)
    prediction_rbf = classifier_rbf.predict(test_vectors)

    # Perform classification with SVM, kernel=linear
    classifier_linear = svm.SVC(kernel='linear')
    classifier_linear.fit(train_vectors, train_labels)
    prediction_linear = classifier_linear.predict(test_vectors)

    # Perform classification with SVM, kernel=linear
    classifier_liblinear = svm.LinearSVC()
    classifier_liblinear.fit(train_vectors, train_labels)
    prediction_liblinear = classifier_liblinear.predict(test_vectors)

    # Print results
    print("Results for SVC(kernel=rbf)")
    print(classification_report(test_labels, prediction_rbf))
    print("Results for SVC(kernel=linear)")
    print(classification_report(test_labels, prediction_linear))
    print("Results for LinearSVC()")
    print(classification_report(test_labels, prediction_liblinear))

        