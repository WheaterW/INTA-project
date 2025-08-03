Dragonfly Topology
==================

Each network node in a direct topology is directly connected to a compute node, and no network device is specially used to interconnect network nodes. That is, in a direct topology, all devices are leaf nodes; there are no spine nodes typical of a traditional topology. The dragonfly topology is the most widely used direct topology. In the dragonfly topology, there are multiple groups, with full-mesh connections established between groups and within a group. This means each pair of groups are connected through one or more links; each network node in a group is directly connected to other network nodes in the group and can also be connected to other groups and compute nodes.

**Figure 1** Dragonfly topology  
![](figure/en-us_image_0000001513150422.png)

Each network node can support the following link types simultaneously:

* Global link: also called an inter-group link, connects nodes in different groups. A node's port, when connected to a global link, is called a global port.
* Local link: also called an intra-group link, connects nodes in the same group. A node's port, when connected to a local link, is called a local port.
* Access link: connects network nodes and compute nodes. A node's port, when connected to an access link, is called an access port.

**Figure 2** Comparison between adaptive routing networking and topology  
![](figure/en-us_image_0000001564110485.png)
#### Planning Suggestions

In the dragonfly topology, the sum of bandwidths between each network node and other network nodes in the same group is represented by a, the sum of bandwidths between each network node and compute nodes is represented by p, and the sum of bandwidths between each network node and other groups is represented by h. To achieve better load balancing, it is recommended that the following condition be met: a = 2p = 2h. If other values are used, the following conditions must be met: a â¥2h and 2p â¥ 2h. To ensure better network performance, it is recommended that device interfaces be fully used. The link planning suggestions for networks of different scales are as follows:

* Small-scale networking: Each network node in a group is connected to all the other groups through multiple parallel links.
* Medium-scale networking: Each network node in a group is connected to all the other groups through one link.
* Large-scale networking: Each pair of groups is connected through one link.

**Figure 3** Dragonfly networking scenarios  
![](figure/en-us_image_0000001512830870.png)