import sys
import os
import json

# import the JSON array
def loadStorageData():
    input_file = open('storages.json')
    storages = json.load(input_file)
    return storages

# sort function to sort based on capacity
def sortFunction(json):
    return json["capacity"]

# Sort our storages in an ascending depending on capacity.
def getSortedByCapacity():
    storages = loadStorageData()
    sortedStorages = sorted(storages, key=sortFunction)
    return sortedStorages

# Return all storages that have enough capacity, iops, and throughput.
def findAllViableStorages():
    viableStorages = []
    storages = getSortedByCapacity()
    requestedCapacity = int(sys.argv[2])
    requestedIOPS = int(sys.argv[3])
    requestedThroughput = int(sys.argv[4])

    for i in range(len(storages)):
        if storages[i]["capacity"] >= requestedCapacity and storages[i]["iops"] >= requestedIOPS and storages[i]["throughput"] >= requestedThroughput:
            viableStorages.append(storages[i])

    return viableStorages

def calculateScore(storage):
    requestedCapacity = int(sys.argv[2]) #In TB
    requestedIOPS = int(sys.argv[3])
    requestedThroughput = int(sys.argv[4]) # GB/s
    #capacityMulti = 1
    #iopsMulti = 0.7
    #throughputMulti = 0.7
    score =  (storage["capacity"] -  requestedCapacity) * 100 + storage["iops"] - requestedIOPS + storage["throughput"] - requestedThroughput * 1000
    return score

# Find the best match from the storages
def findOptimalStorage():
    storages = findAllViableStorages()
    best_storage = {}
    best_score = float('inf') # Infinity represents a very large number
    # We need to pick the one with the least score in order to best utilize our resources.
    for storage in storages:
        tmp = calculateScore(storage)
        if tmp < best_score:
            best_score = tmp
            best_storage = storage
    return best_storage

def eprint(*args, **kwargs):
        print(*args, file=sys.stderr, **kwargs)

def validate_args():
    if len(sys.argv) != 4:
        eprint("Please supply the path of the data set path and the request paramters")
        eprint("Usage: python3 compute.py <currentStoragesjson> <requestcapacity> <requestiops> <requestthroughput>")
        exit(1)

def main():
    print(findOptimalStorage())

main()
