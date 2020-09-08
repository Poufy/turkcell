import sys
import os
import json

# Total Capacity, IOPS, Throughput
totalCapacity = 0
totalIOPS = 0
totalThroughput = 0

# import the JSON array
def loadStorageData():
    input_file = open('storages.json')
    storages = json.load(input_file)
    return storages

# sort function to sort based on a certain JSON attribute.
def sortFunction(json):
    return json["capacity"]

def getMultiplier(resource):
    input_file = open('priority.json')
    multipliers = json.load(input_file)
    return multipliers[resource]

# Sort our storages in an ascending depending on capacity.
def getSortedStorages():
    storages = loadStorageData()
    sortedStorages = sorted(storages, key=sortFunction)
    return sortedStorages

def increaseTotalAttributes(storage):
    global totalCapacity, totalIOPS, totalThroughput
    totalCapacity += storage["capacity"]
    totalIOPS += storage["iops"]
    totalThroughput += storage["throughput"]

# This returns a value between 0 and 1 to use in the scoring.
def normalizeData(value, total):
    return value/total

def calculateScore(storage):
    #Normalizing the requested data
    requestedCapacity = normalizeData(int(sys.argv[2]), totalCapacity) #In TB
    requestedIOPS = normalizeData(int(sys.argv[3]), totalIOPS)
    requestedThroughput = normalizeData(int(sys.argv[4]), totalThroughput) # GB/s

    #Normalizing the storage data
    storageCapacity = normalizeData(storage["capacity"], totalCapacity)
    storageIOPS = normalizeData(storage["iops"], totalIOPS)
    storageThroughput = normalizeData(storage["throughput"], totalThroughput)

    #Getting the Multipliers from priority.json
    capacityMulti = getMultiplier("capacityMulti")
    IOPSMulti = getMultiplier("IOPSMulti")
    throughputMulti = getMultiplier("throughputMulti")

    score =  (storageCapacity - requestedCapacity * capacityMulti) +  (storageIOPS - requestedIOPS * IOPSMulti) + (storageThroughput - requestedThroughput * throughputMulti)

    return score

# Return all storages that have enough capacity, iops, and throughput.
def findAllViableStorages():
    viableStorages = []
    storages = loadStorageData()
    requestedCapacity = int(sys.argv[2])
    requestedIOPS = int(sys.argv[3])
    requestedThroughput = int(sys.argv[4])

    for i in range(len(storages)):
        if storages[i]["capacity"] >= requestedCapacity and storages[i]["iops"] >= requestedIOPS and storages[i]["throughput"] >= requestedThroughput:
            viableStorages.append(storages[i])
            increaseTotalAttributes(storages[i])
    return viableStorages

# Find the best match from the storages
def findOptimalStorage():
    storages = findAllViableStorages()
    best_storage = {}
    best_score = float('inf') # Infinity represents a very large number
    # We need to pick the one with the least score in order to best utilize our resources.
    for storage in storages:
        tmp = calculateScore(storage)
        print("Score: " + str(tmp) + " with wwn: " + str(storage["wwn"]))
        if tmp < best_score:
            best_score = tmp
            best_storage = storage
    return best_storage

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def validate_args():
    if len(sys.argv) != 5:
        eprint("Please supply the path of the data set path and the request paramters")
        eprint("Usage: python3 compute.py <currentStoragesjson> <requestcapacity> <requestiops> <requestthroughput>")
        exit(1)

def main():
    validate_args()
    result = findOptimalStorage()
    print("The best choice is: " + str(result))

main()
