Overview of IP Hard Pipe
========================

Overview_of_IP_Hard_Pipe

#### Definition

IP hard pipe is an IP-network-based access technology that strictly isolates soft and hard pipes by reserving hardware resources on routers. The hard pipe can preempt the bandwidth resources of the soft pipe while not being affected by soft pipe congestion. The hard pipe can provide guaranteed bandwidth and low delay for the private line services of high-value customers.

In the IP hard pipe solution, a controller is used to manage bandwidth resources network-wide. The physical interface bandwidth on the public network is divided and allocated to hard and soft pipes. For example, on a 10GE interface, 2 Gbit/s bandwidth is allocated to the hard pipe, and the remaining 8 Gbit/s is allocated to the soft pipe. The hard and soft pipes are isolated. The hard pipe can preempt the bandwidth resources of the soft pipe, but the soft pipe cannot preempt the bandwidth of the hard pipe.

**Figure 1** IP hard pipe networking  
![](images/fig_feature_image_0006367152.png "Click to enlarge")

#### Purpose

Customers that have high requirements on bandwidth, delay, and security prefer synchronous digital hierarchy (SDH) networks. To retain these customers, carriers must keep both IP and SDH networks, resulting in heavy maintenance. Therefore, carriers expect to migrate the customer network to the IP network to reduce maintenance costs and facilitate user management.

IP hard pipe has been developed to meet up with this expectation. It provides bandwidth guarantee and low delay on IP networks, allowing IP networks to provide access services with SDH service quality. It also provides service-specific OAM and SLA monitoring, helping accelerate the migration of SDH networks to IP private lines.


#### Benefits

IP hard pipe offers the following benefits to carriers:

* Deployment of high-quality private lines for VIP customers on newly deployed or existing routers, minimizing SDH network construction and cutting costs for maintaining both SDH and IP networks
* Rapid service protection, ensuring high-reliability service quality
* IP FPM-based granular service quality measurement, providing flexible and effective maintenance and management of the private lines for VIP customers