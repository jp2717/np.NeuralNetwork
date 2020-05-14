from mlxtend.data import loadlocal_mnist #library to import MNIST 

#imports mnist data from current directory
#Inputs: None
#Outputs: dataset as a list of tuples, with each tuple being a (feature,label) pair


#function that returns mnist data in the form of a tuple of tuples, with each tuple containing an input-output pair
def mnist_data():
    print("Loading MNIST data...")
    X, y = loadlocal_mnist(
        images_path='data/train-images-idx3-ubyte', 
        labels_path='data/train-labels-idx1-ubyte')

    print("MNIST data loaded succesfully.")
    #make list of tuples of (Xi, yi) format
    dataset = [] #empty list

    print("Reformatting MNIST data...")
    for Xi, yi in zip(X,y):
        combo = (Xi,yi)
        dataset.append(combo)
    print("Reformatting MNIST data was successful.")
    return dataset

    #code testing:
    # print(mnist_data[0]) #expected output is a tuple containing a numpy image array and label