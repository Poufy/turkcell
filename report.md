# Introduction

We need to find the optimal storage to choose from a pool of storages in order to utilize the overall storage capacity. A certain amount of Capacity, IOPS, Throughput will be requested, and we need to find the most optimal storage to assign these resources.

# Approach

Initial solution: Assign the Capacity, IOPS, Throughput to the storage with the least capacity that is enough and make sure it has enough IOPS and Throughput. For example: If we have 2 storage devices, one with 30/40 TB and the other with 20/40 TB and the request requires 10TB of storage, we will choose the one with 30/40 TB.

Reasoning: This approach will always utilize the capacity over all the existing storages.

If we have 2 storages both with the same capacity like 30/40TB and the request requires 10TB then we will look at other resources like IOPS and Throughput to find the one that matches best.

