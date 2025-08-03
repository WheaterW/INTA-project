Overview of IPv6 Multicast Route Management
===========================================

Overview of IPv6 Multicast Route Management

#### Definition

IPv6 multicast route management involves creating or changing IPv6 multicast routes to control the forwarding of multicast packets, as well as detecting and maintaining multicast forwarding paths.


#### Purpose

With IPv6 multicast route management, multicast route creation can be controlled or multicast reverse path forwarding (RPF) routes can be changed to control multicast routing and forwarding.

IPv6 multicast route management provides the following functions:

* RPF check
  
  This function is used to find the optimal unicast route to a multicast source and build a multicast distribution tree (MDT). In the unicast route, the outbound interface functions as the inbound interface of data in a forwarding entry. When the forwarding module receives a multicast data packet, it matches the packet against the forwarding entry and checks whether the inbound interface of the packet is correct. If the inbound interface of the packet is identical to the outbound interface of the unicast route, the packet passes the RPF check; otherwise, the packet fails the RPF check and is discarded. RPF checks prevent traffic loops in multicast data forwarding.
* Multicast static route
  
  Multicast static routes are an important basis for RPF checks. By configuring multicast static routes, you can specify RPF interfaces and RPF neighbors for packets with specific sources.
* Multicast load splitting
  
  During multicast routing, a multicast load splitting policy enables the selection of unique equal-cost routes as RPF routes for different forwarding entries to guide data forwarding. As the RPF routes on which the forwarding entries depend are hashed to different equal-cost routes, multicast data flows are then split.
* Multicast boundary
  
  Multicast boundary allows multicast information of each multicast group to be transmitted within a specified scope. After multicast boundary is configured for a multicast group on an interface of a multicast device, a closed multicast forwarding area is formed, and the interface will not send or receive packets of the multicast group.