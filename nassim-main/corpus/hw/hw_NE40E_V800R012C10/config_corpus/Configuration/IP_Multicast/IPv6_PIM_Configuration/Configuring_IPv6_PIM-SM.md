Configuring IPv6 PIM-SM
=======================

On a PIM-SM network, any sender can be a multicast source, and receivers cannot know multicast source addresses before they join multicast groups. A Rendezvous Point (RP) is the forwarding core on a PIM-SM network. RPs are categorized as embedded-RPs, static RPs, BootStrap router (BSR) RPs, responsible for collecting multicast source information and group member information.

#### Usage Scenario

PIM-SM is for use on large-scale networks where group members are sparsely distributed and receivers do not need to specify a multicast source when joining a multicast group. An RP is the forwarding core on a PIM-SM network. It collects information about group members and multicast sources.

* After creating a (\*, G) entry for a new IGMP member relationship, the receiver's Designated router (DR) sends a Join/Prune message to the RP.
* When a multicast source starts to send data to a group, the source's DR unicasts a Register message to the RP. The RP de-encapsulates the Register message and forwards the data to other multicast members along the rendezvous point tree (RPT).
* RP switches traffic from the RPT to the shortest path tree (SPT), and then the RP sends a Register-Stop message to the source's DR.

On an IPv6 network, PIM-SM supports the following types of RPs:

* Embedded-RP
  
  By default, an embedded-RP is started. The range of groups served by an embedded-RP is limited. To avoid inconsistent RP election results, an embedded RP takes preference over a static or BSR RP.
* Static RP
  
  To use a static RP, manually configure the same RP address on each Router in the PIM-SM domain. Static RPs apply to small-scale PIM networks with stable topologies. To enhance the robustness and the operation management of a multicast network, a static RP is usually used as a backup of a dynamic RP.
* BSR RP
  
  To use a BSR RP, select several Routers in the PIM-SM domain and configure them as C-RPs and C-BSRs. Then, an RP is automatically elected in the PIM-SM domain. Each Router in the PIM-SM domain knows the location of the RP.

A multicast group may be in the service ranges of an embedded-RP, a BSR RP, and a static RP simultaneously. The default sequence used by Routers to select an RP for such groups is embedded-RP > BSR RP > static RP.

Compared with a scheme in which all groups correspond to a single RP, a scheme in which different multicast groups correspond to different RPs reduces the load on individual RPs, making the network more robust.


#### Pre-configuration Tasks

Before configuring IPv6 PIM-SM, configure an IPv6 unicast routing protocol to ensure that IPv6 unicast routes are reachable.


[Enabling IPv6 Multicast Routing](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2006.html)

Enable IPv6 multicast routing on a Router before you configure other IPv6 multicast features on the Router.

[Enabling IPv6 PIM-SM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2007.html)

To enable a Router interface to establish IPv6 PIM neighbor relationships with other Routers, enable IPv6 PIM-SM.

[Configuring an Embedded-RP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2008.html)

By default, the embedded-Rendezvous Point (RP) function is enabled. You can change the range of IPv6 multicast groups that an embedded RP serves or disable the embedded-RP function.

[Configuring a Static RP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2009.html)

To use a static Rendezvous Point (RP) in an IPv6 PIM-SM domain, configure the same RP address and same address arrange of multicast groups that the RP serves on all Routers in the IPv6 PIM-SM domain.

[Configuring a BSR RP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2010.html)

Select several Routers and configure them as Candidate-BootStrap Routers (C-BSRs) and Candidate-Rendezvous Points (C-RPs). A BSR is dynamically elected from C-BSRs. The BSR collects C-RP information and summarizes C-RP information into an RP-Set. The RP-Set is encapsulated in a Bootstrap message and advertised to all the Routers in the IPv6 PIM domain. Then, the C-RPs elect a BSR RP based on a uniform election rule.

[(Optional) Setting a Multicast Source Address Range](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2011.html)

You can configure multicast source addresses-based filtering policies by creating IPv6 ACLs. Then, an IPv6 PIM Router forwards only the multicast packets whose source address or source/group addresses match the IPv6 ACLs.

[(Optional) Adjusting Source Registration Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2012.html)

A new multicast source must register with a Rendezvous Point (RP). You can configure policies of filtering Register messages on the Candidate-Rendezvous Points (C-RPs) and set the holdtime of the register-suppression state and the interval for sending null Register messages on the source's DR or disable the source's DR from sending Register messages.

[(Optional) Configuring SPT Switchover Conditions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2013.html)

PIM-SM enables a Rendezvous Point (RP) or a receiver's Designated router (DR) to trigger a shortest path tree (SPT) switchover when the rate of IPv6 multicast packets is high. You can configure the SPT switchover conditions and the interval for checking the rate at which IPv6 multicast data is forwarded on the receiver's DR.

[(Optional) Configuring a Limit on the Number of PIM-SM Entries](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_ipv6vrf.html)

IPv6 PIM-SM allows you to limit the number of (S, G) and (\*, G) entries separately. After a specified limit is reached, new entries of the corresponding type cannot be created.

[Verifying the IPv6 PIM-SM Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2014.html)

After configuring IPv6 PIM-SM, verify information about BootStrap routers (BSRs), Rendezvous Points (RPs), PIM interfaces, PIM neighbors, and PIM routing tables.