Overview of BGP4+
=================

BGP4+ controls route advertisement and selects optimal routes.

#### BGP4+ Definition

As a dynamic routing protocol used between ASs, BGP4+ is an extension of BGP.

Traditional BGP4 manages IPv4 routing information but does not support the inter-AS transmission of packets encapsulated by other network layer protocols (such as IPv6).

To support IPv6, BGP4 must have the additional ability to associate an IPv6 protocol with the next hop information and network layer reachable information (NLRI).

Two NLRI attributes that were introduced to BGP4+ are as follows:

* Multiprotocol Reachable NLRI (MP\_REACH\_NLRI): carries the set of reachable destinations and the next hop information.
  
  **Figure 1** MP\_REACH\_NLRI structure  
  ![](figure/en-us_image_0000001507484422.png)
  
  **Table 1** Fields in MP\_REACH\_NLRI
  | Field | Length | Description |
  | --- | --- | --- |
  | AFI (address family identifier) | 2 bytes | Indicates the address class to which the network layer protocol belongs. It is used to specify the carried IPv6 reachable route information. |
  | SAFI (subsequent address family identifier) | 1 byte | Indicates that the attribute carries information about reachable IPv6 unicast routes. |
  | Length of Next Hop Network Address | 1 byte | Indicates the length of bytes occupied by the next hop. The value 16 indicates that the link-local address is not included, and the value 32 indicates that the link-local address is included. |
  | Network Address of Next Hop | Variable | Indicates information about the next-hop address to the destination network, which may contain a link-local address. |
  | Number of SNPAs | 1 byte | Indicates a reserved bit. The value is 0. |
  | Network Layer Reachability Information | Variable | Indicates carried IPv6 reachable route information, including the IPv6 prefix. |
* Multiprotocol Unreachable NLRI (MP\_UNREACH\_NLRI): carries the set of unreachable destinations.
  
  **Figure 2** MP\_UNREACH\_NLRI structure  
  ![](figure/en-us_image_0000001507804218.png)
  
  **Table 2** Fields in MP\_UNREACH\_NLRI
  | Field | Length | Description |
  | --- | --- | --- |
  | AFI (Address Family Identifier) | 2 bytes | Indicates that the attribute carries information about unreachable IPv6 routes. |
  | SAFI (subsequent address family identifier) | 1 byte | Indicates that the attribute carries information about unreachable IPv6 unicast routes. |
  | Network Layer UnReachability Information | 1 byte | Indicates the carried IPv6 unreachable route information. |

The Next\_Hop attribute in BGP4+ is in the format of an IPv6 address, which can be either a globally unique IPv6 address or a next hop link-local address.

Using multiple protocol extensions of BGP, BGP4+ is applicable to IPv6 networks without changing the messaging and routing mechanisms of BGP.


#### Purpose

BGP transmits route information between ASs. It, however, is not required in all scenarios.

**Figure 3** BGP networking  
![](images/fig_feature_image_0003997160.png)  

BGP is required in the following scenarios:

* On the network shown in [Figure 3](#EN-US_CONCEPT_0172366421__en-us_concept_0172354362_fig_dc_vrp_bgp_feature_000101), users need to be connected to two or more ISPs. The ISPs need to provide all or part of the Internet routes for the users. Devices, therefore, need to select the optimal route through the AS of an ISP to the destination based on the attributes carried in BGP routes.
* The AS\_Path attribute needs to be transmitted between users in different organizations.
* Users need to transmit VPN routes through a Layer 3 VPN. For details, see the *HUAWEI NE40E-M2 series Feature Description - VPN*.
* Users need to transmit multicast routes to construct a multicast topology. For details, see *HUAWEI NE40E-M2 series Feature Description - IP Multicast*.

BGP is not required in the following scenarios:

* Users are connected to only one ISP.
* The ISP does not need to provide Internet routes for users.
* ASs are connected through default routes.