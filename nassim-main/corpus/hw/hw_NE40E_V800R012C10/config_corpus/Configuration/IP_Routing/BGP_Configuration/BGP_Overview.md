BGP Overview
============

The Border Gateway Protocol (BGP) advertises and maintains a large number of routes between autonomous systems (ASs).

#### BGP Definition

Border Gateway Protocol (BGP) is a dynamic routing protocol used between autonomous systems (ASs).

It exchanges reachable routing information between ASs, establishes inter-AS paths, prevents routing loops, and applies routing policies between ASs. BGP has three earlier versions: BGP-1, BGP-2, and BGP-3.

Currently, BGP-4 is used.

As an exterior routing protocol on the Internet, BGP has been widely used among Internet service providers (ISPs).

BGP has the following characteristics:

* Unlike an Interior Gateway Protocol (IGP), such as Open Shortest Path First (OSPF) and Routing Information Protocol (RIP), BGP is an Exterior Gateway Protocol (EGP) which controls route advertisement and selects optimal routes between ASs rather than discovering or calculating routes.
* BGP uses Transport Control Protocol (TCP) as the transport layer protocol, which enhances BGP reliability.
  
  + BGP selects inter-AS routes, which poses high requirements on stability. Therefore, using TCP enhances BGP's stability.
  + BGP peers must be logically connected through TCP. The destination port number is 179 and the local port number is a random value.
* BGP supports Classless Inter-Domain Routing (CIDR).
* When routes are updated, BGP transmits only the updated routes, which reduces bandwidth consumption during BGP route distribution. Therefore, BGP is applicable to the Internet where a large number of routes are transmitted.
* BGP is a distance-vector routing protocol.
* BGP is designed to prevent loops.
  
  + Between ASs: BGP routes carry information about the ASs along the path. The routes that carry the local AS number are discarded to prevent inter-AS loops.
  + Within an AS: BGP does not advertise routes learned in an AS to BGP peers in the AS to prevent intra-AS loops.
* BGP provides many routing policies to flexibly select and filter routes.
* BGP provides a mechanism for preventing route flapping, improving Internet stability.
* BGP can be easily extended to adapt to network development.

#### Purpose

BGP transmits route information between ASs. It, however, is not required in all scenarios.

**Figure 1** BGP networking  
![](images/fig_feature_image_0003997160.png)  

BGP is required in the following scenarios:

* On the network shown in [Figure 1](#EN-US_CONCEPT_0172366123__en-us_concept_0172354362_fig_dc_vrp_bgp_feature_000101), users need to be connected to two or more ISPs. The ISPs need to provide all or part of the Internet routes for the users. Devices, therefore, need to select the optimal route through the AS of an ISP to the destination based on the attributes carried in BGP routes.
* The AS\_Path attribute needs to be transmitted between users in different organizations.
* Users need to transmit VPN routes through a Layer 3 VPN. For details, see the *HUAWEI NE40E-M2 series Feature Description - VPN*.
* Users need to transmit multicast routes to construct a multicast topology. For details, see *HUAWEI NE40E-M2 series Feature Description - IP Multicast*.

BGP is not required in the following scenarios:

* Users are connected to only one ISP.
* The ISP does not need to provide Internet routes for users.
* ASs are connected through default routes.