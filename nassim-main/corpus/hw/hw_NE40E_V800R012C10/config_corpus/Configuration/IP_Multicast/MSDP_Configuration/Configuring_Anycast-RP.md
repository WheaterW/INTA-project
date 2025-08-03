Configuring Anycast-RP
======================

Anycast-RP allows you to configure several Rendezvous Points (RPs) with the same address in a PIM-SM domain. Peer relationships are established between RPs so that the multicast source can register with the topologically closest RP and the multicast receiver can join the closest RP. This alleviates burdens on RPs, implements RP backup, and optimizes multicast forwarding paths.

#### Usage Scenario

In a traditional PIM-SM domain, each multicast group is mapped only to one RP. When the network is overloaded or traffic congests on an RP, the following problems may occur:

* The RP is overloaded.
* Routes converge slowly after the RP fails.
* The multicast forwarding path is not optimal.

Compared with the traditional PIM-SM network, the multicast network deployed with Anycast-RP has the following advantages:

* RP load balancing
  
  Each RP maintains only partial source and group information in the PIM-SM domain, and forwards partial multicast data.
* RP redundancy
  
  After an RP fails, the multicast sources that register with it and the receivers that join it select another near RP to register with and join.
* RP optimal path
  
  + Receivers send Join messages to the nearest RP, so rendezvous point trees (RPTs) have the optimal paths.
  + Multicast sources register with the nearest RP, so SPTs have the optimal paths.

#### Pre-configuration Tasks

Before configuring Anycast-RP, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* Enable multicast routing on all Routers and PIM-SM on all Router interfaces.
* Configure a PIM-SM domain without any RP.


[Configuring an RP Address on a Loopback Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0051.html)

Before configuring Anycast-Rendezvous Point (RP) on Routers in a PIM-SM domain, specify a loopback interface on each Router and assign the same IP address to the loopback interfaces. In addition, configure the Routers to advertise the RP address through unicast routes to ensure that each Router has a reachable route to the RPs.

[Configuring a Loopback Interface as an RP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0052.html)

You can configure a loopback interface as either a static Rendezvous Point (RP) or a Candidate-Rendezvous Point (C-RP). To configure a static RP, perform the configuration on all the Routers in the PIM-SM domain; to configure a C-RP, perform the configuration only on the Routers where Anycast-RP is to be configured.

[Configuring MSDP Peers on RPs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0053.html)

MSDP peer relationships need to be set up between Rendezvous Points (RPs). If there are more than three Routers, MSDP peer relationships must be set up between any two Routers and all MSDP peers must be added to one mesh group.

[Specifying a Logical RP Address for SA Messages](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0054.html)

An MSDP peer performs the Reverse Path Forwarding (RPF) check on received Source Active (SA) messages. If the remote Rendezvous Point (RP) address carried in the SA message is the same as the local RP address, the MSDP peer discards the SA message. Therefore, you need to specify a logical RP address for the SA messages on the Router on which Anycast-RP is to be configured.

[Verifying the RP Configuration in a PIM-SM Domain](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0055.html)

After configuring Anycast-Rendezvous Point (RP) in a PIM-SM domain, verify information about MSDP peers and RP information of PIM routing entries.