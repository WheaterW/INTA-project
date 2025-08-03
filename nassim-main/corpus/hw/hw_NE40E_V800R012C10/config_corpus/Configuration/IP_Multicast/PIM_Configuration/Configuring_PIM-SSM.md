Configuring PIM-SSM
===================

The PIM-SSM model provides the source-specific transmission service for receivers. In PIM-SSM, a dedicated multicast forwarding path is set up directly between a source and a receiver.

#### Usage Scenario

PIM-SSM adopts partial PIM-SM technologies. In Protocol Independent Multicast-Source-Specific Multicast (PIM-SSM), there is no need for Rendezvous Point (RP) mapping, rendezvous point tree (RPT) construction, or multicast source registration. In PIM-SSM, the Designated router (DR) is valid only on the shared network segment connected with group members. After learning the requirements of users, the receiver's DR sends a Join message to the multicast source. The Join message is sent upstream hop by hop and (S, G) entries are created correspondingly. As a result, a shortest path tree (SPT) from the Router directly connected to the source to the receiver's DR is set up.

To implement PIM-SSM, the following conditions must be met:

* The multicast group that users join is in the SSM group address range.
* Users specify the source when joining a multicast group.
* All Routers run PIM-SM.

A network can adopt both the PIM-SM and PIM-SSM models. To implement PIM-SSM, first complete PIM-SM configurations, including RP configurations. Then, adjust the SSM group address range as needed. If the groups that hosts want to join are not in the SSM group address range, PIM-SM is adopted to forward multicast data.


#### Pre-configuration Tasks

Before configuring PIM-SSM, configure a unicast routing protocol to ensure that unicast routes are reachable.


[Enabling Multicast Routing](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2182a.html)

Enable multicast routing on a Router before you configure other multicast features on the Router.

[Enabling PIM-SM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2183a.html)

To enable a Router interface to establish PIM neighbor relationships with other Routers, enable PIM-SM.

[Setting an SSM Group Address Range](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0024.html)

Protocol Independent Multicast-Source-Specific Multicast (PIM-SSM) and PIM-SM have different group address ranges. If the group that a host joins is in the SSM group address range, PIM-SSM is adopted for multicast data forwarding; otherwise, PIM-SM is adopted. The default SSM group address range is 232.0.0.0/8, and the SSM group address range can be modified.

[(Optional) Configuring a Limit on the Number of PIM Entries](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_1035.html)

PIM-SSM allows you to limit the number of (S, G) entries. After a specified limit is reached, new (S, G) entries are not created.

[(Optional) Setting a Multicast Source Address Range](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2184b.html)

You can configure multicast source addresses-based filtering policies by creating ACLs. Then, a PIM Router forwards only the multicast packets whose source address or source/group addresses match the ACLs.

[(Optional) Configuring Multicast Source Proxy on an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_3155.html)



[Verifying the PIM-SSM Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0025.html)

After the Protocol Independent Multicast-Source-Specific Multicast (PIM-SSM) is configured, verify information about PIM interfaces, PIM neighbors, and PIM routing tables.