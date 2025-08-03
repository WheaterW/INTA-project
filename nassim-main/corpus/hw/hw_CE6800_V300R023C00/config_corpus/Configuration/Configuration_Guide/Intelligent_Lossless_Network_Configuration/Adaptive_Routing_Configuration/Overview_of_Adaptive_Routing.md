Overview of Adaptive Routing
============================

Overview of Adaptive Routing

#### Definition

The adaptive routing technology dynamically determines routes based on the network topology and traffic load changes. By proactively detecting the link congestion status, adaptive routing preferentially selects a short and non-congested packet forwarding path to improve network throughput and resilience, as well as reduce network latency.


#### Purpose

Building a large supercomputing center requires interconnection between a large number of compute nodes. However, expanding the cluster scale increases the network latency and deployment costs, failing to meet requirements regarding computing power and deployment. A direct topology features large-scale access and a small network diameter. In such a topology, adaptive routing can be deployed to achieve the following: When network links are normal, the shortest path is preferentially selected to forward packets. When the shortest path is congested, a non-shortest path that is not congested is selected to forward packets. In this way, network links are fully utilized to improve bandwidth utilization, meeting the requirements of high throughput, low latency, and low costs while supporting large-scale networking.