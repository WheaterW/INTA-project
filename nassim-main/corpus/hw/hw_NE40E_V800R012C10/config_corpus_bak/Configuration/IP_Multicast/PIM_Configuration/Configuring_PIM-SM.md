Configuring PIM-SM
==================

On a PIM-SM network, any sender can be a multicast source, and receivers cannot know multicast source addresses before they join multicast groups. A Rendezvous Point (RP) is the forwarding core on a PIM-SM network. RPs are categorized as static RPs or BootStrap router (BSR) RPs, responsible for collecting multicast source information and group member information.

#### Usage Scenario

On a large-scale network where multicast group members are sparsely located and receivers do not need to specify multicast sources when they join multicast groups, you can configure PIM-SM. An RP is the forwarding core on a PIM-SM network. Group members and the multicast source converge at the RP.

* After creating a (\*, G) entry for a new IGMP member relationship, the receiver's Designated router (DR) sends a Join/Prune message to the RP.
* When a multicast source starts to send data to a group, the source's DR unicasts a Register message to the RP. After receiving the Register message, the RP decapsulates it and then forwards the data to other multicast members along the rendezvous point tree (RPT).
* The RP switches traffic from the RPT to the shortest path tree (SPT), and then the RP sends a Register-Stop message to the source's DR.

PIM-SM supports static RPs and BSR RPs.

* Static RP
  
  To use a static RP, manually configure the same RP address on each Router in the PIM-SM domain. Static RPs apply to small-scale PIM networks with stable topologies. To enhance the robustness and the operation management of a multicast network, a static RP is usually used as a backup of a dynamic RP.
* BSR RP
  
  To use a BSR RP, select several Routers in the PIM-SM domain and configure them as Candidate-Rendezvous Points (C-RPs) and Candidate-BootStrap Routers (C-BSRs). Then, an RP is automatically elected in the PIM-SM domain.

A multicast group may be in the service ranges of both the BSR RP and static RP. By default, the Router preferentially selects the BSR RP unless the static RP is configured to be preferentially selected.

Configuring an RP to serve only one multicast group is recommended. This can reduce the load of a single RP and enhance network robustness.


#### Pre-configuration Tasks

Before configuring PIM-SM, configure a unicast routing protocol to ensure that unicast routes are reachable.


[Enabling Multicast Routing](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0007.html)

Enable multicast routing on a Router before you configure other multicast features on the Router.

[Enabling PIM-SM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0008.html)

To enable a Router interface to establish PIM neighbor relationships with other Routers, enable PIM-SM.

[Configuring a Static RP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0009.html)

To use a static Rendezvous Point (RP) in a PIM-SM domain, configure the same RP address and same address range of multicast groups that the RP serves on all Routers in the PIM-SM domain.

[Configuring a BSR RP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0010.html)

Select several Routers and configure them as Candidate-BootStrap Routers (C-BSRs) and Candidate-Rendezvous Points (C-RPs). A BSR is dynamically elected from C-BSRs. The BSR collects C-RP information and summarizes C-RP information into an RP-Set. The RP-Set is encapsulated in a Bootstrap message and advertised to all the Routers in the PIM domain. Then, the C-RPs elect a BSR RP based on a uniform election rule.

[(Optional) Configuring a Limit on the Number of PIM-SM Entries](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_ipv4vrf.html)

PIM-SM allows you to limit the number of (S, G) and (\*, G) entries separately. After a specified limit is reached, new entries of the corresponding type cannot be created.

[(Optional) Setting a Multicast Source Address Range](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0011.html)

You can configure multicast source addresses-based filtering policies by creating ACLs. Then, a PIM Router forwards only the multicast packets whose source address or source/group addresses match the ACLs.

[(Optional) Adjusting Source Registration Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0012.html)

A new multicast source must register with a Rendezvous Point (RP). You can configure policies of filtering Register messages on the Candidate-Rendezvous Points (C-RPs) and configure a device to calculate the checksum of each Register message based on all the contents of a Register message. In addition, you can set the holdtime of the register-suppression state and the interval for sending null Register messages on the source's Designated router (DR) or disable the source's DR from sending Register messages.

[(Optional) Configuring Multicast Source Proxy on an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_3153.html)



[(Optional) Configuring SPT Switchover Conditions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0013.html)

PIM-SM allows a Rendezvous Point (RP) or a receiver's Designated router (DR) to trigger a shortest path tree (SPT) switchover when the rate of multicast packets is high. You can configure SPT switchover conditions and set the interval for checking the forwarding rate of multicast packets on the receiver's DR.

[Verifying the PIM-SM Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0014.html)

After PIM-SM is configured, verify information about BootStrap routers (BSRs), rendezvous points (RPs), PIM interfaces, PIM neighbors, and PIM routing tables.