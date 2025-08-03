Configuring Distributed MAP-E
=============================

Configuring Distributed MAP-E

#### Distributed Scenario

In a distributed scenario, the MAP-BR and BRAS reside on the same device. The device functions as the BRAS to deliver MAP addresses and mapping rules to MAP-CEs in DHCPv6 IA\_PD mode. (In this example, only key configurations of IPv6 address assignment are provided. For details, see *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - User Access - IPv6 Address Management Configuration*.) The device also functions as a MAP-BR and resides on the edge of a MAP domain. The device allows the MAP-CEs to access the public IPv4 network through the IPv6 network that is within the MAP domain. In addition, the MAP-CEs can use each other's public IPv4 address to communicate through the MAP-BR.

**Figure 1** Distributed MAP-E  
![](images/fig_dc_ne_map_cfg_0036.png)

#### Configuration Roadmap

In the distributed scenario, MAP-E is configured on the MAP-BR (BRAS).


[Configuring a BMR](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0022_mape_dis.html)

This section describes how to configure a basic mapping rule (BMR). A BMR is used to convert user-side IPv6 addresses into IPv4 addresses and network-side IPv4 addresses into IPv6 addresses.

[Configuring a BR](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0014_mape_dis.html)

A border relay (BR) is created. The MAP-CE encapsulates an IPv6 prefix defined based on the BR into traffic and directs the traffic to an interface board. The MAP-CE then selects a MAP-E instance to convert the traffic.

[Configuring an IPv6 Delegation Prefix Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0032_dis_mape.html)

In a MAP-E or MAP-T scenario, a MAP rule needs to be bound to an IPv6 delegation prefix pool. The NE40E uses the BMR configured using the **map-rule** command to assign prefixes to MAP users.

[Configuring an IPv6 Delegation Address Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0035_dis_mape.html)

In a MAP-E scenario, a prefix pool, a BR device name, and an FMR flag bit need to be configured in an IPv6 delegation address pool.

[Binding a BR to a MAP-E Instance](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0015_distributed.html)

This section describes how to bind a BR to a MAP-E instance so that a MAP-CE selects a MAP-E instance to convert IPv6 packets after MAP processing.

[Binding a BMR to a MAP-E Instance](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0016_distributed.html)

This section describes how to bind a BMR to a MAP-E instance. The BMR is used to encapsulate and verify packets in the MAP-E instance.

[(Optional) Setting an MSS Value for MAP-E Services](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0017_distributed.html)

The maximum segment size (MSS) value defined in TCP specifies the maximum length of a TCP packet to be sent without fragmentation. Two devices exchange SYN packets to negotiate the MSS value for a TCP connection to be established. If the size of packets for MAP processing is larger than a link MTU, the packets are fragmented. You can reduce the MSS value in TCP, which prevents a service board from fragmenting packets and helps improve MAP efficiency.

[(Optional) Setting the Traffic Class of IPv6 Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0019_distributed.html)

When an IPv4 packet is translated into an IPv6 packet, the Traffic-Class field value in the IPv6 packet is copied from the ToS field in the IPv4 packet. To modify the traffic class of IPv6 packets, set the traffic class value of IPv6 packets in an instance.

[Checking the Configurations](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0020_distributed.html)

After configuring basic MAP-E functions, verify the configurations.