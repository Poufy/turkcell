import sys
import os

class compute(self):

    def getWWN(self):
        print("wwn")

    def getCapacity(self):
        print("capacity in compute")

    def getIops(self):
        print("iops")

    def getThroughput():
        print("throughput")

    def findOptimalStorage(self, filename):
        print('Optimal Storage of {0}'.format(filename))

def eprint(*args, **kwargs):
        print(*args, file=sys.stderr, **kwargs)

def validate_args():
    if len(sys.argv) != 2:
        eprint("Please supply the path of the data set path")
        eprint("Usage: python3 compute.py <datasetname>")
        exit(1)

def main():
    validate_args()
    obj = compute()
    obj.findOptimalStorage(sys.argv[1])

main()
