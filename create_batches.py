from mnist_data import mnist_data

#takes in the data and splits our data into separate mini-batches

#Input: dataset in the format of a list of tuples (feature,label) and a batch sizes
#Output: list of batches of a given batch size

def create_batches(dataset,batch_size):
    batches = [] #creating a list of batches

    print("Creating batches of batch size = ",batch_size,"...")
    for idx in range(0,len(dataset),batch_size): #for each tuple in the given dataset
        if idx+batch_size < len(dataset): #if we can still make a full batch
            batch = dataset[idx:idx+batch_size]
        else:
            batch = dataset[idx:]
        batches.append(batch) #add the batch to our list of batches of the given batch size
    
    print("Batches created successfully.")
    return batches

#Code test: expected output is the first tuple pair of (feature,label)
# dataset = mnist_data()
# batches = create_batches(dataset,4)
# print(batches[0][0])

