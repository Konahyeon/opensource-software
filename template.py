#PLEASE WRITE THE GITHUB URL BELOW!
# https://github.com/Konahyeon/opensource-software.git

import sys
import pandas as pd

def load_dataset(dataset_path):
	#To-Do: Implement this function
	dataset_df = pd.read_csv(dataset_path)
	return dataset_df

def dataset_stat(dataset_df):	
	#To-Do: Implement this function
	n_feats = dataset_df.shape[1] - 1
	n_class0 = dataset_df.groupby('target').size()[0]
	n_class1 = dataset_df.groupby('target').size()[1]
	return n_feats, n_class0, n_class1


def split_dataset(dataset_df, testset_size):
	#To-Do: Implement this function
	print("\n안뇽1")

def decision_tree_train_test(x_train, x_test, y_train, y_test):
	#To-Do: Implement this function
	print("\n안뇽2")

def random_forest_train_test(x_train, x_test, y_train, y_test):
	#To-Do: Implement this function
	print("\n안뇽3")

def svm_train_test(x_train, x_test, y_train, y_test):
	#To-Do: Implement this function
	print("\n안뇽4")

def print_performances(acc, prec, recall):
	#Do not modify this function!
	print ("Accuracy: ", acc)
	print ("Precision: ", prec)
	print ("Recall: ", recall)

if __name__ == '__main__':
	#Do not modify the main script!
	data_path = sys.argv[1]
	data_df = load_dataset(data_path)

	n_feats, n_class0, n_class1 = dataset_stat(data_df)
	print ("Number of features: ", n_feats)
	print ("Number of class 0 data entries: ", n_class0)
	print ("Number of class 1 data entries: ", n_class1)

	print ("\nSplitting the dataset with the test size of ", float(sys.argv[2]))
	x_train, x_test, y_train, y_test = split_dataset(data_df, float(sys.argv[2]))

	acc, prec, recall = decision_tree_train_test(x_train, x_test, y_train, y_test)
	print ("\nDecision Tree Performances")
	print_performances(acc, prec, recall)

	acc, prec, recall = random_forest_train_test(x_train, x_test, y_train, y_test)
	print ("\nRandom Forest Performances")
	print_performances(acc, prec, recall)

	acc, prec, recall = svm_train_test(x_train, x_test, y_train, y_test)
	print ("\nSVM Performances")
	print_performances(acc, prec, recall)