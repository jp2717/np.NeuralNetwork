#function that takes in a given dataset of inputs and outputs and splits it into training, test and validation data
import numpy as np
import random
# from data_loader import mnist_data

#Input: dataset in the format of a list of tuples, where tuples are the pair (feature,label)
#Output: training, testing and validation datasets in the same format

#I have chosen to take a ratio of 8:1:1 of the full dataset respectively for each

def split_data(dataset):
    print("Splitting dataset into training, testing and validation...")

#applying random shuffling to our list
    random.shuffle(dataset)
    datasize = len(dataset) 

    train_size = int(round(0.8*datasize))
    test_size = int(round(0.1*datasize))
    val_size = int(round(0.1*datasize))

    train_data = dataset[0:train_size]
    test_data = dataset[train_size : train_size + test_size]
    val_data = dataset[train_size + test_size : train_size + test_size + val_size]

    print("Dataset was split succesfully.")
    return train_data,test_data,val_data

#code testing: expected output is that the lengths of each dataset set should add up to the original's length
# print(len(dataset),len(train_data),len(test_data),len(val_data))