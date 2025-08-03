Understanding Single-Hop or Multi-Hop BFD
=========================================

Understanding Single-Hop or Multi-Hop BFD

#### Related Concepts

A BFD session can be set up on an IP link for quick fault detection. BFD for IP can monitor single- and multi-hop IPv4 and IPv6 links

* Single-hop BFD checks IP connectivity between two directly connected systems. A single hop refers to one IP hop. Between these two systems, only one BFD session can be set up for a specified data protocol on a specified interface.
* Multi-hop BFD monitors all paths between two systems. The paths may span multiple hops or partially overlap.

#### Application Scenarios

**Typical application 1: single-hop BFD**

As shown in [Figure 1](#EN-US_CONCEPT_0000001176741801__fig_dc_vrp_bfd_feature_000401), BFD monitors the single-hop IP path between DeviceA and DeviceB, and BFD sessions are bound to outbound interfaces.

**Figure 1** Single-hop BFD  
![](figure/en-us_image_0000001130622380.png)

**Typical application 2: multi-hop BFD**

As shown in [Figure 2](#EN-US_CONCEPT_0000001176741801__fig_dc_vrp_bfd_feature_000402), BFD monitors the multi-hop IP path between DeviceA and DeviceC, and BFD sessions are bound to peer IP addresses instead of outbound interfaces.

**Figure 2** Multi-hop BFD  
![](figure/en-us_image_0000001176741825.png)