Overview of BGP4+
=================

Overview of BGP4+

#### Definition

Border Gateway Protocol (BGP) is a dynamic routing protocol used between autonomous systems (ASs). BGP-4, which is capable of carrying routing information for IPv4 only, is the most commonly used version of BGP. Multiprotocol extensions for BGP-4, commonly referred to as BGP4+, enable BGP to carry routing information for multiple network layer protocols, such as IPv6.


#### Purpose

BGP4+ transmits routes between ASs; however, it may not be required in some situations.

BGP4+ is required in the following situations:

* If a user needs to connect to two or more ISPs that need to provide partial or all Internet routes for the user, as shown in [Figure 1](#EN-US_CONCEPT_0000001130622416__en-us_concept_0172354362_fig_dc_vrp_bgp_feature_000101). In such situations, devices can select the optimal route through the AS of an ISP to the destination based on the attributes carried in BGP4+ routes.
* If the AS\_Path information needs to be transmitted between users from different organizations.

**Figure 1** BGP4+ application scenario  
![](figure/en-us_image_0000001130782238.png)

BGP4+ is not required in the following situations:

* If users connect to only one ISP.
* If an ISP does not need to provide Internet routes for users.
* If the default route is used for communication between ASs.