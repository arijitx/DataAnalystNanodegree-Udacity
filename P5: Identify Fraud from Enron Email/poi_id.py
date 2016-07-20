#!/usr/bin/python

import sys
import pickle
sys.path.append("tools/")

#Function for new Feature creation
def compute_fraction( poi_messages, all_messages ):
    fraction = 0.
    if poi_messages!='NaN':
        fraction=int(poi_messages)/float(all_messages)
    return fraction


from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
print "13 Features Selected . . ."
features_list = ['poi','salary','bonus','deferred_income','director_fees','exercised_stock_options'
                ,'expenses','fraction_from_poi','fraction_to_poi','loan_advances','long_term_incentive'
                 ,'restricted_stock','total_payments','total_stock_value']
# You will need to use more features

### Load the dictionary containing the dataset
print "Loading Dataset . . ."
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)


### Task 2: Remove outliers
print "Removing Outlier . . ."
del data_dict['TOTAL']
### Task 3: Create new feature(s)
print "Creating New Features . . ."
for k,v in data_dict.iteritems():
	data_dict[k]['fraction_from_poi']=compute_fraction(data_dict[k]['from_poi_to_this_person'],data_dict[k]['to_messages'])
	data_dict[k]['fraction_to_poi']=compute_fraction(data_dict[k]['from_this_person_to_poi'],data_dict[k]['from_messages'])

### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

from sklearn.feature_selection import SelectKBest,f_classif
from sklearn import preprocessing
from sklearn.pipeline import Pipeline
mms = preprocessing.MinMaxScaler()
kbest=SelectKBest(f_classif, k=5)



from sklearn.cross_validation import train_test_split
from sklearn import metrics
ftrain, ftest, ltrain, ltest = train_test_split(features, labels, test_size=0.3, random_state=42)

def printPerformance(pred):
	print '------------------------------------'
	print 'Precision ',metrics.precision_score(ltest,pred)
	print 'Recall ',metrics.recall_score(ltest,pred)
	print 'F1_score ',metrics.f1_score(ltest,pred)
### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
p_gnb =  Pipeline(steps=[('scaling', mms),("kbest", kbest), ("GaussianNB", GaussianNB())])
p_dtree= Pipeline(steps=[('scaling', mms),("kbest", kbest), ("Dtree", DecisionTreeClassifier(random_state=0))])
p_svc= Pipeline(steps=[('scaling', mms),("kbest", kbest), ("LinearSVC", LinearSVC())])

p_gnb.fit(ftrain,ltrain)
print 'GaussianNB Performance'
printPerformance(p_gnb.predict(ftest))

p_dtree.fit(ftrain,ltrain)
print 'Dtree Performance'
printPerformance(p_dtree.predict(ftest))

p_svc.fit(ftrain,ltrain)
print 'SVM Performance'
printPerformance(p_svc.predict(ftest))


### Task 5: Tune your classifier to achieve better than .3 precision and recall 

parameters = {'Dtree__criterion':('gini', 'entropy'),'Dtree__min_samples_split':list(xrange(3,5)),'Dtree__min_samples_leaf':list(xrange(3,10))}
from sklearn.grid_search import GridSearchCV

p_dtree2= Pipeline(steps=[('scaling', mms),("kbest", kbest), ("Dtree", DecisionTreeClassifier(random_state=0))])

p_dtree_tuned = GridSearchCV(estimator=p_dtree2, param_grid=parameters,scoring='f1')
p_dtree_tuned.fit(ftrain,ltrain)
pred=p_dtree_tuned.predict(ftest)
print 'Decision Tree Performance'
printPerformance(pred)
print p_dtree_tuned.best_params_

clf=p_gnb

##Validation
print 'Validation'
p_gnb.fit(ftrain,ltrain)
print 'GaussianNB Performance'
printPerformance(p_gnb.predict(ftest))
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
# from sklearn.cross_validation import train_test_split
# features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(p_gnb, my_dataset, features_list)