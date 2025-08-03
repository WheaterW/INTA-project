Eth-Trunk Fundamentals
======================

In [Figure 1](#EN-US_CONCEPT_0000001176661229__fig418633916713), DeviceA and DeviceB are connected through three physical Ethernet links. These links are bundled into one logical link, and their bandwidths add up to the bandwidth of the logical link. The three physical Ethernet links back each other up so that traffic can switch to other functional member links if an active link fails. The end result of Eth-Trunk is improved reliability.

**Figure 1** Eth-Trunk networking  
![](figure/en-us_image_0000001176741201.gif)

Eth-Trunk basic concepts are described as follows.

#### LAG and LAG Interface

[Figure 2](#EN-US_CONCEPT_0000001176661229__fig1790794654518) shows a LAG, which is a logical link composed of multiple physical Ethernet links, so it is also called an Eth-Trunk.

Each LAG has one logical interface, known as a LAG interface or Eth-Trunk interface, which can be treated as a common Ethernet interface to implement routing and other services. In contrast to physical Ethernet interfaces, an Eth-Trunk interface needs to select one or more member interfaces to forward traffic.


#### Member Interface and Member Link

In [Figure 2](#EN-US_CONCEPT_0000001176661229__fig1790794654518), the interfaces that constitute an Eth-Trunk interface are known as member interfaces, and the link corresponding to a member interface is known as a member link.

**Figure 2** Relationship between the LAG, LAG interface, member interface, and member link  
![](figure/en-us_image_0000001130781536.png)

#### Active and Inactive Interfaces and Links

There are two types of interfaces in a LAG: active interfaces that forward data and inactive interfaces that do not forward data.

The link connected to an active interface is an active link, and that connected to an inactive interface is an inactive link.


#### Upper Threshold for the Number of Active Interfaces

Capping the number of active interfaces is used to improve network reliability while assuring bandwidth. When the number of active interfaces reaches the upper threshold, this number will no longer increase even if you add new member interfaces to the Eth-Trunk interface. Links connected to the excess member interfaces you have added will be set to the down state and function as backup links.

For example, 8 fully-functioning member links bundle into an Eth-Trunk, with each link providing a bandwidth of 1 Gbit/s. If the Eth-Trunk only needs to provide a maximum bandwidth of 5 Gbit/s, you can set the maximum number of up member links to 5. Then any unselected links automatically enter the backup state, improving reliability.

Configuring the upper threshold for the number of active interfaces is not applicable to the link aggregation in manual mode.


#### Lower Threshold for the Number of Active Interfaces

When the number of active interfaces falls below the lower threshold, the Eth-Trunk interface goes down. Configuring the lower threshold for the number of active interfaces in an Eth-Trunk ensures that the Eth-Trunk has the minimum required bandwidth. If two devices are connected through an Eth-Trunk and other links, when the Eth-Trunk goes down because the number of active interfaces falls below the lower threshold, traffic will be switched to standby links for transmission.


#### Link Aggregation Mode

Link aggregation can work in manual or Link Aggregation Control Protocol (LACP) mode. For details, see [Eth-Trunk in Manual Mode](vrp_eth-trunk_cfg_0005.html) and [Eth-Trunk in LACP Mode](vrp_eth-trunk_cfg_0006.html).