# The Problem

We would like to automate the process of installing new servers to the system. We would like to choose a storage so that we can optimize the overall resouces of the system. A certrain capacity, IOPS, and throughput will be requested and we need to find the optimal storage to assign these resources.


## Solution Idea

A simple solution but very efficient and scalable.

The idea is we need to find the storage that fits our request best without wasting any resources.

For example: If we have a 30/40 TB storage and a 20/40 TB storage and the request is asking for 10TB then we will assign it the storage with 30/40. But we have to apply this idea to all the fields including IOPS and Throughput.

## Implementation

Here is an overview of the structure.

```bash
compute.py extractor.py storages.json priority.json
```

extractor.py is responsible for extracting the data of the existing storages and converting them into json format and output them inside the storages.json file.

### Computing the Result

compute.py will take the JSON array supplied by storages.json and filter it over multiple steps in order to find the best match.

First we loop over the all the existing storages to find the storages that have enough capacity/iops/throughput

(loop pic)[filter.jpg]

Now once we have an array of all the viable storages we need to know which one fits the best. In order to do that we need to calculate a score for each resource
