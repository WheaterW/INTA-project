Overview of GTSM
================

Overview of GTSM

#### Definition

The Generalized TTL Security Mechanism (GTSM), a protection mechanism based on the time to live (TTL) value, checks whether the TTL value in the IP packet header is within a pre-defined range and discards invalid packets to protect TCP/IP-based control plane protocols from CPU overload attacks.


#### Purpose

An attacker simulates a routing protocol and continuously sends packets to a device. If the device cannot determine the validity of packets, the device is busy processing attack packets, resulting in CPU overload attacks.

In this case, a method is required to check the validity of packets. GTSM can be used to check the TTL value in the packet header.

The main function of TTL values is to prevent IP packets from being circulated over a network in infinite loops. The maximum TTL value is 255. The TTL value is decremented by 1 each time a packet passes through a hop. Since the number of hops between any two routing neighbors is limited by the network scale and structure, the TTL values of protocol packets exchanged between the devices are confined to a particular range.

Based on network conditions, the TTL value range used between routing neighbors can be predefined. In this way, devices can check the validity of TTL values in packets to determine packet validity and filter out invalid packets (attack packets).


#### Fundamentals

As shown in [Figure 1](#EN-US_CONCEPT_0000001176661593__fig12430124014436):

* IGP connections are established to implement connectivity between devices.
* A BGP connection is established between DeviceA and DeviceB.
* An attacker remotely accesses the network from the Internet, simulates BGP negotiation packets, and continuously sends packets to DeviceA or DeviceB.

When DeviceA and DeviceB negotiate a BGP peer relationship, one path can be selected from three for packet forwarding. The number of hops (including the last hop) on the selected path through which the packets pass may be 3, 5, or 6. That is, a maximum of six hops are possible.

In this situation, GTSM can be used to predefine the TTL value range as [255 â 6 + 1, 255], that is, [250, 255]. Remote BGP attack packets whose TTL values are not within the specified range are considered invalid and are dropped.

**Figure 1** GTSM Attack Defense Fundamentals  
![](figure/en-us_image_0000001130622052.png)

Although planning and configuring TTL value ranges become complex on a complex network, you can define a generally appropriate range based on network conditions to allow GTSM to filter out attack packets as many as possible, since their TTL values are out of the specified range.