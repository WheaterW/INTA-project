Subnetting
==========

A network can be divided into multiple subnets to conserve IPv4 address space and support flexible IPv4 addressing.

When many hosts are distributed on an internal network, the internal host IDs can be divided into multiple subnet IDs to facilitate management. In this case, the entire network contains multiple small networks.

The network ID of subnets is visible to the external network, but the subnet IDs are not. The subnet IDs take effect in route selection and destination host addressing only after datagrams enter the internal network.

[Figure 1](#EN-US_CONCEPT_0000001176743243__fig_dc_fd_IPv4_000701) shows subnetting of a Class B IPv4 address. The subnet mask consists of a string of continuous 1s and 0s. All 1s correspond to the Net-id and Subnet-id fields, and all 0s correspond to the Host-id field.

**Figure 1** IPv4 address subnetting  
![](figure/en-us_image_0000001176663397.png "Click to enlarge")

The Class B IP address shown in [Figure 1](#EN-US_CONCEPT_0000001176743243__fig_dc_fd_IPv4_000701) is used as an example. Assume that the network address is 172.16.0.0 and the mask is 255.255.0.0. The two most significant bits of the host ID are used for subnetting. The subnet ID ranges from 00 to 11 (binary), allowing a maximum of 4 (22) subnets. Each subnet ID has a subnet mask, which changes after subnetting. Specifically, the subnet mask of the Class B IP address is changed from 255.255.0.0 to 255.255.192.0. After performing an AND operation on the IPv4 address and the subnet mask, you can obtain the network address. [Figure 2](#EN-US_CONCEPT_0000001176743243__fig_dc_fd_IPv4_000702) shows the network addresses of the four subnets.

**Figure 2** IPv4 address subnets  
![](figure/en-us_image_0000001176743311.png "Click to enlarge")

[Table 1](#EN-US_CONCEPT_0000001176743243__table_01) lists the network addresses (with the all-0 host ID), broadcast addresses (with the all-1 host ID), and host addresses of the preceding four subnets.

**Table 1** Network address and host address ranges (in binary format)
| Subnet | Network Address | Broadcast Address | Host Address Range |
| --- | --- | --- | --- |
| 10101100 00010000 00000000 00000000 | 10101100 00010000 00000000 00000000 | 10101100 00010000 00111111 11111111 | 10101100 00010000 00000000 00000001  to  10101100 00010000 00111111 11111110 |
| 10101100 00010000 01000000 00000000 | 10101100 00010000 01000000 00000000 | 10101100 00010000 01111111 11111111 | 10101100 00010000 01000000 00000001  to  10101100 00010000 01111111 11111110 |
| 10101100 00010000 10000000 00000000 | 10101100 00010000 10000000 00000000 | 10101100 00010000 10111111 11111111 | 10101100 00010000 10000000 00000001  to  10101100 00010000 10111111 11111110 |
| 10101100 00010000 11000000 00000000 | 10101100 00010000 11000000 00000000 | 10101100 00010000 11111111 11111111 | 10101100 00010000 11000000 00000001  to  10101100 00010000 11111111 11111110 |

Typically, the subnetting result is presented in decimal format. Converting a result in binary format to that in decimal format is complex. The following describes how to conveniently divide a network into subnets in decimal notation.

Take the preceding Class B IP address with the network address of 172.16.0.0 and the mask of 255.255.0.0 as an example. After subnetting, the subnet mask is 255.255.192.0. The length of the subnet mask equals 18 (16 + 2) bits. The calculation method is as follows:

* The number of bits in a subnet ID is *m*, and the number of subnets is 2*m*. In this example, *m* equals 2, so the number of subnets is 4.
* The number of bits in a host ID is *n*, and the number of valid host addresses in each subnet is 2*n* - 2 (excluding the number of host addresses that comprise all 1s or all 0s). In this example, *n* equals 14, so the number of valid host addresses in each subnet is 16382.
* The span between two neighboring subnet IDs is called block size, which is the value of deducting a subnet mask that is neither 0.0.0.0 nor 255.255.255.255 from 256. The first subnet network ID starts from 0 (located in the subnet mask in decimal format that is neither 0.0.0.0 nor 255.255.255.255), and the IDs of the following subnets increase individually by block size. In this example, the block size is 64 (256 - 192). The four subnets are 172.16.**0**.0/18, 172.16.**64**.0/18, 172.16.**128**.0/18, and 172.16.**192**.0/18, respectively.

[Table 2](#EN-US_CONCEPT_0000001176743243__table_02) lists the subnetting result in decimal format.

**Table 2** Network address and host address ranges (in decimal format)
| Subnet | Network Address | Broadcast Address | Host Address Range |
| --- | --- | --- | --- |
| 172.16.0.0/18 | 172.16.0.0 | 172.16.63.255 | 172.16.0.1 to 172.16.63.254 |
| 172.16.64.0/18 | 172.16.64.0 | 172.16.127.255 | 172.16.64.1 to 172.16.127.254 |
| 172.16.128.0/18 | 172.16.128.0 | 172.16.191.255 | 172.16.128.1 to 172.16.191.254 |
| 172.16.192.0/18 | 172.16.192.0 | 172.16.255.255 | 172.16.192.1 to 172.16.255.254 |

Borrowing bits from the Host-id field to create a Subnet-id field reduces the number of supported hosts. For example, a Class B IP address can contain 65534 (216 - 2) host addresses. If a 2-bit Subnet-id field is created, the four subnets have a maximum of 65528 [4 x (214 - 2)] host addresses, which is six less than the number of host addresses when no 2-bit Subnet-id field is created.

To implement efficient network planning, subnetting and IPv4 addressing should abide by the rules described below.

#### Hierarchy

To divide a network into multiple layers, you need to consider geographic and service factors. Use a top-down subnetting mode to facilitate network management and simplify routing tables. Generally:

* A network consisting of a backbone network and a metro network is divided into hierarchical subnets.
* An administrative network is divided into subnets based on administrative levels.

#### Consecutiveness

Consecutive addresses facilitate route summarization on a hierarchical network, which greatly reduces the number of routing entries and improves route searching efficiency. When allocating IP addresses, note the following:

* Allocate consecutive IP addresses to each area.
* Allocate consecutive IP addresses to devices that have the same services and functions.

#### Scalability

When allocating addresses, reserve certain addresses at each layer to ensure consecutive address allocation in future network expansion.

A backbone network must have sufficient consecutive addresses for independent autonomous systems (ASs) and further network expansion.


#### Efficiency

When planning subnets, fully utilize address resources to ensure that the subnets are sufficient for hosts.

* Allocate IP addresses by using variable length subnet mask (VLSM) to fully utilize address resources.
* Consider the routing mechanism in subnetting to improve address utilization in the allocated address space.