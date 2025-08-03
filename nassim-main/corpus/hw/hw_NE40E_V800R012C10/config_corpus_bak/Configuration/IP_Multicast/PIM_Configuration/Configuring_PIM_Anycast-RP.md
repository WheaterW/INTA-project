Configuring PIM Anycast-RP
==========================

Anycast-RP is a feature supporting the configuration of several Rendezvous Points (RPs) with the same address in a PIM-SM domain. Peer relationships are established between RPs so that IP routing can automatically select the topologically closest RP for each source and receiver. This alleviates burdens on RPs, implements RP backup, and optimizes multicast forwarding paths.

#### Usage Scenario

In a traditional PIM-SM domain, each multicast group is mapped only to one RP. When the network is overloaded or traffic congests on an RP, many network problems occur. For example, the RP may be overloaded, routes may converge slowly if the RP fails, or the multicast forwarding path may not be optimal.

To resolve these issues, configure PIM Anycast-RP. PIM Anycast-RP is an intra-domain feature. To enable an RP to obtain information about the multicast source in another PIM-SM domain, you can adopt either of the following schemes:

* Set up Multicast Source Discovery Protocol (MSDP) peer relationships between every Anycast-RP member in a PIM-SM domain and the RP in another PIM-SM domain.
* Set up MSDP peer relationships between some Anycast-RP members with the RP in another PIM-SM domain. After the members who have set up MSDP peer relationships receive SA messages, they extract source and group information from SA messages, encapsulate the information into Register messages, and forward the Register messages to the members who do not set up MSDP peer relationships with the RP.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Anycast-RP can be implemented in a PIM-SM domain by using the MSDP Anycast-RP or PIM Anycast-RP. In IPv4 network deployment, you can choose either of the two schemes. Mixed use of the two schemes is not recommended.



#### Pre-configuration Tasks

Before configuring the PIM Anycast-RP, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* [Configure PIM-SM](dc_vrp_multicast_cfg_0006.html).


[Configuring Global Anycast-RP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2148.html)

If Anycast-RP is configured on some devices in a PIM-SM domain, configure the address of the Rendezvous Point (RP) elected in the PIM-SM domain as the Anycast-RP address.

[Configuring a Local Address for an Anycast-RP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2149.html)

When sending a PIM Register message to all Anycast-RP peers, the local Rendezvous Point (RP) needs to use its own IP address (called the local address) as the source address of the Register message.

[Configuring an Anycast-RP Peer](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2150.html)

When sending a PIM Register message to all Anycast-Rendezvous Point (RP) peers, the local RP needs to use the peer addresses as the destination addresses of the Register message.

[Verifying the Configuration of the PIM Anycast-Rendezvous Point (RP)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2151.html)

After configuring PIM Anycast-Rendezvous Point (RP), verify the Anycast-RP configuration.