Overview of BGP
===============

Overview of BGP

#### Definition

Border Gateway Protocol (BGP) is a dynamic routing protocol used between autonomous systems (ASs).

BGP exchanges reachable routing information between ASs, establishes inter-AS paths, prevents routing loops, and applies routing policies between ASs. BGP has three earlier versions: BGP-1, BGP-2, and BGP-3.

BGP-4 is the current version of BGP.


#### Purpose

As an exterior routing protocol on the Internet, BGP is widely used between Internet service providers (ISPs). [Figure 1](#EN-US_CONCEPT_0000001130783948__en-us_concept_0172354362_fig_dc_vrp_bgp_feature_000101) shows an application scenario of BGP.

**Figure 1** Application scenario of BGP  
![](figure/en-us_image_0000001130624242.png)

BGP transmits routes between ASs; however, it may not be required in some situations.

BGP is required in the following situations:

* A user needs to be connected to two or more ISPs, and the ISPs need to provide all or part of the Internet routes for the user. In such situations, devices can select the optimal route through the AS of an ISP to the destination based on the attributes carried in BGP routes.
* The AS\_Path attribute needs to be transmitted between users in different organizations.

BGP is not required in the following situations (at least one of them is met):

* Users are connected to only one ISP.
* The ISP does not need to provide Internet routes for users.
* ASs communicate with each other through default routes.