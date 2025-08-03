Overview of PIM
===============

Protocol Independent Multicast (PIM) is an intra-domain multicast routing protocol that uses unicast routing information to perform reverse path forwarding (RPF) checks on multicast packets and to create multicast routing entries. PIM can dynamically respond to network topology changes and maintain multicast forwarding tables.

"Protocol Independent" indicates that the unicast routing protocol that provides unicast routing information for PIM can be a static route or a dynamic routing protocol, such as Routing Information Protocol (RIP), Open Shortest Path First (OSPF), Intermediate-System to Intermediate-System (IS-IS), or Border Gateway Protocol (BGP). Multicast routing entries are generated based on a unicast routing table.

PIM implements multicast packet forwarding by means of the RPF mechanism. The RPF mechanism uses existing unicast routing information to build an MDT on a network. When a multicast packet reaches a Router, the Router performs the RPF check first.

* If the multicast packet passes the RPF check, the Router creates a multicast routing entry and forwards the packet.
* If the multicast packet fails the RPF check, the Router discards the packet.

#### PIM Mode

PIM has PIM-DM, PIM-SM, and PIM-SSM modes. PIM-SM and PIM-SSM apply to IPv4 and IPv6 networks, and PIM-DM applies only to IPv4 networks. The ASM group address range is used by PIM-DM, and PIM-SM, and the SSM group address range is used by PIM-SSM.

* PIM-DM
  
  The PIM-DM mode applies to a small-scale network with densely distributed members. The key mechanisms of PIM-DM are neighbor discovery, flooding, prune, graft, assert, and status refresh.
* PIM-SM
  
  PIM-SM applies to large-scale networks on which multicast data receivers are sparsely distributed. Key PIM-SM mechanisms include neighbor discovery, assert, designated router (DR) election, RP discovery, Join, Prune, Register, and SPT switchover.
* PIM-SSM
  
  PIM-SSM applies to networks on which multicast data receivers can learn source locations before they join multicast groups and require multicast data from specific multicast sources. PIM-SSM adopts only some of PIM-SM technologies. PIM-SSM does not need to maintain an RP, construct RPTs, or register multicast sources. In PIM-SSM, an SPT can be built directly between the source's DR and the receiver's DR.

#### PIM Routing Entry

A PIM routing table records PIM routing entries and delivers them to a multicast forwarding table to guide multicast packet forwarding. PIM routing entries are categorized as (S, G) or (\*, G) entries. In PIM routing entries, S indicates a multicast source address, G indicates a multicast group address, and \* indicates any multicast source address.

* An (S, G) entry is created for a multicast packet that carries a specified source address and a specified group address.
* An (\*, G) entry is created for a multicast packet that carries a specified group address but does not carry a specified source address.

When a PIM device receives a multicast packet with the source address being S and the group address being G and the packet passes the RPF check, the router forwards the packet based on the following rules:

* If a matching (S, G) entry exists, the router forwards the packet along the route specified by the (S, G) entry.
* If a matching (S, G) entry does not exist, the router creates an (S, G) entry, and then forwards the packet along the route specified by the (S, G) entry.

PIM routing entries contain the following information: multicast source addresses, multicast group addresses, upstream interfaces, upstream neighbors, and downstream interface lists. A multicast packet reaches from a unique upstream interface and is forwarded through one or multiple downstream interfaces. [Figure 1](#EN-US_CONCEPT_0172366785__fig_dc_vrp_multicast_cfg_000401) shows the forwarding process of multicast packets (with the group address 225.1.1.1) on DeviceA.

**Figure 1** Multicast packet forwarding![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1, 2, and 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](images/fig_dc_vrp_multicast_cfg_000401.png)

The following example uses the PIM routing table on DeviceA shown in [Figure 1](#EN-US_CONCEPT_0172366785__fig_dc_vrp_multicast_cfg_000401).

```
<DeviceA> display pim routing-table

 VPN-instance: public net
 Total 0 (*, G) entry; 1 (S, G) entry
 (10.1.8.1, 225.1.1.1)
```
```
     RP: 2.2.2.2
```
```
     Protocol: pim-sm, Flag: SPT ACT
```
```
     UpTime: 01:35:25
```
```
     Upstream interface: GigabitEthernet0/2/0
```
```
         Upstream neighbor: 10.1.2.2
```
```
         RPF prime neighbor: 10.1.2.2
```
```
     Downstream interface(s) information:
```
```
     Total number of downstreams: 2
```
```
        1: GigabitEthernet0/3/0
```
```
            Protocol: igmp, UpTime: 00:03:21, Expires: 00:03:10
```
```
        2: GigabitEthernet0/1/0
```
```
            Protocol: pim-sm, UpTime: 00:03:27, Expires: 00:03:15
```

The information used to guide packet forwarding is as follows:

* Source address: 10.1.8.1
* Group address: 225.1.1.1
* Upstream interface: GE 0/2/0
* Upstream neighbor: 10.1.2.2
* RPF neighbor: 10.1.2.2 (DeviceB)
* Downstream interface list: includes interfaces GE 0/1/0 and GE 0/3/0