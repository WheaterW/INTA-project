Configuring OSPFv3 Attributes on Different Types of Networks
============================================================

By setting network types for OSPFv3 interfaces and adjusting OSPFv3 attributes, you can build OSPFv3 networks flexibly.

#### Usage Scenario

Based on the types of link layer protocols, OSPFv3 classifies networks into the following types:

* P2MP: Because P2MP is not a link layer protocol, each P2MP network is changed from a network of another type.
* NBMA: If the link layer protocol is X.25, OSPFv3 defaults the network type to NBMA.
* Broadcast: If the link layer protocol is GigabitEthernet or FDDI, OSPFv3 defaults the network type to broadcast.
* P2P: If the link layer protocol is PPP, HDLC or, LAPB, OSPFv3 defaults the network type to P2P.

You can change network types and configure OSPFv3 features to flexibly build networks without changing link layer protocols.


#### Pre-configuration Tasks

Before configuring OSPFv3 attributes on different types of networks, complete the following tasks:

* Configure a link layer protocol.
* Configure IPv6 addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic OSPFv3 functions](dc_vrp_ospfv3_cfg_2003.html).

#### Configuration Procedures

**Figure 1** Flowchart for configuring OSPFv3 attributes on different types of networks  
![](images/fig_dc_vrp_ospfv3_cfg_200801.png)


[Configuring the Network Type for an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2009.html)

OSPFv3 classifies networks into broadcast, P2P, P2MP, and NBMA networks based on link layer protocols. By setting the network type of an interface, you can forcibly change the network type of the interface.

[(Optional) Setting the DR Priority for the OSPFv3 Broadcast or NBMA Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2010.html)

You can specify the Designated Router (DR) priority for each interface on a broadcast or a non-broadcast multiple access (NBMA) network for DR/Backup Designated Router (BDR) election on the network.

[(Optional) Setting the Polling Interval at Which Hello Packets Are Sent on an NBMA Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2011.html)

On an NBMA network, a device sends Hello packets to a neighbor that is Down at a polling interval.

[(Optional) Disabling MTU Check on DD Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2012.html)

After you prevent an interface from checking the Maximum Transmission Unit (MTU) field in received Database Description (DD) packets, the device can receive packets with the MTU field as 0.

[Verifying the Configuration of OSPFv3 Attributes in Different Types of Networks](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2013.html)

After configuring attributes of OSPFv3 interfaces on different types of networks, verify information about OSPFv3 interfaces.