Configuring Distributed MAP-T
=============================

Configuring_Distributed_MAP-T

#### Distributed Scenario

In a distributed scenario, the MAP-BR and BRAS reside on the same device. The device functions as the BRAS to deliver MAP addresses and mapping rules to MAP-CEs in DHCPv6 IA\_PD mode. (In this example, only key configurations of IPv6 address assignment are provided. For details, see *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - User Access - IPv6 Address Management Configuration*.) The device also functions as a MAP-BR and resides on the edge of a MAP domain. The device allows the MAP-CEs to access the public IPv4 network through the IPv6 network that is within the MAP domain. In addition, the MAP-CEs can use each other's public IPv4 address to communicate through the MAP-BR.

**Figure 1** Distributed MAP-T  
![](images/fig_dc_ne_map_cfg_0036.png)

#### Configuration Roadmap

In the distributed scenario, MAP-T is configured on the MAP-BR (BRAS).


[Configuring a BMR](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0022_bras_distributed.html)

This section describes how to configure a basic mapping rule (BMR). Configure BMR rules on the BRAS to instruct the BRAS to assign IPv6 and IPv4 addresses to MAP-CEs.

[Configuring a DMR](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0004_distributed.html)

A default mapping rule (DMR) can be created. A MAP-CE encapsulates an IPv6 prefix defined in the DMR into packets and directs the packets to a service board. Address translation is performed in the bound MAP-T instance.

[Configuring an IPv6 Prefix Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0032_1_distributed.html)

In distributed MAP-T scenarios, IPv6 prefix pools can be configured in either delegation or remote mode. In delegation mode, the BMR configured using the **map-rule** command is used to assign prefixes to MAP users. When a device functions as a DHCPv6 relay agent, it uses an IPv6 remote prefix pool to manage prefixes.

[Configuring an IPv6 Address Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0033_1_distributed.html)

In a distributed MAP-T scenario, a prefix pool, a DMR prefix, and an FMR flag bit need to be configured in an IPv6 delegation address pool. An IPv6 prefix pool can be configured in either delegation or remote mode. Configuring an IPv6 remote address pool includes binding a prefix pool to the address pool and configuring route advertisement information for the address pool.

[Binding a DMR to a MAP-T Instance](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0005_distributed.html)

This section describes how to bind a DMR to a MAP-T instance. The DMR is used by a MAP-CE to select a MAP-T instance to convert IPv6 packets.

[Binding a BMR to a MAP-T Instance](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0006_distributed.html)

This section describes how to bind a BMR to a MAP-T instance. The BMR is used to encapsulate and verify packets in the MAP-T instance.

[(Optional) Configuring MAP Translation for ICMP/ICMPv6 Error Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0046_distributed.html)

In a MAP-T scenario, the MAP conversion of ICMP error packets can be performed only after the MAP conversion function is configured for ICMP error packets.

[(Optional) Setting an MSS Value for MAP-T Services](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0007_distributed.html)

The MSS value in the TCP protocol is used to specify the length of a TCP packet that can be transmitted without being fragmented. During the TCP connection establishment, the MSS value is carried in a SYN packet to notify the peer end of the maximum size of a packet that can be received by the local end.

[(Optional) Setting the Traffic Class of IPv6 Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0009_distributed.html)

When an IPv4 packet is translated into an IPv6 packet, the Traffic-Class field value in the IPv6 packet is copied from the ToS field in the IPv4 packet. To modify the traffic class of IPv6 packets, set the traffic class value of IPv6 packets in an instance.

[(Optional) Setting an IPv4 ToS Value](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0010_distributed.html)

When an IPv6 packet is translated into an IPv4 packet, the ToS value in the IPv4 packet is copied from the Traffic-Class field in the IPv6 packet by default. To change the ToS value in the IPv4 packet, set the ToS value of the IPv4 packet in an instance.

[(Optional) Clearing the DF Field in IPv4 Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0011_distributed.html)

The default implementation is as follows. Before a device translates an IPv6 packet into an IPv4 packet, if the IPv6 packet does not carry the fragment extension header and the packet length is less than or equal to 1280 bytes, the DF field in the IPv4 packet is set to 0 (can be fragmented). If the IPv6 packet does not carry the fragment extension header and the packet length is greater than 1280 bytes, the DF field in the IPv4 packet is set to 1 (cannot be fragmented). If the IPv6 packet carries the fragment extension header, the DF field in the IPv4 packet is set to 0 (can be fragmented). After the DF field clearing function is enabled, the device sets the DF field in IPv4 packets to 0.

[Checking the Configurations](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0012_distributed.html)

After configuring basic MAP-T functions, verify the configurations.