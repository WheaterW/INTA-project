Configuring IPv6 PIM-SSM
========================

Protocol Independent Multicast-Source-Specific Multicast (PIM-SSM) enables a user to specify a multicast source that will send data to a desired group. PIM-SSM is implemented based on some PIM-SM technologies. In PIM-SSM, no Rendezvous Point (RP) needs to be maintained and a dedicated multicast forwarding path is set up between a receiver and a specified multicast source.

#### Usage Scenario

PIM-SSM uses only some PIM-SM technologies. In PIM-SSM, it is unnecessary to maintain an RP, build a rendezvous point tree (RPT), or register a multicast source. The Designated router (DR) is valid only on a shared network segment connected to group members. Based on users' requirements, the receiver's DR sends a Join message towards the multicast source. The Join message is transmitted upstream hop by hop, and an (S, G) entry is created on each hop. An SPT is built from the Router directly connected to the multicast source to the receiver's DR.

To implement PIM-SSM, the following conditions must be met:

* The IPv6 multicast group that users join is in the SSM group address range.
* Users specify the source when joining an IPv6 multicast group.
* Routers run PIM-SM.

A network can adopt both the PIM-SM and PIM-SSM models. After configuring IPv6 PIM-SM on the network, you can adjust the SSM group address range as needed. If an IPv6 multicast group that a user wants to join is not in the SSM group address range, PIM-SM is adopted to forward IPv6 multicast packets.


#### Pre-configuration Tasks

Before configuring IPv6 PIM-SSM, configure an IPv6 unicast routing protocol to ensure that IPv6 unicast routes are reachable.


[Enabling IPv6 Multicast Routing](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2187b.html)

Enable IPv6 multicast routing on a Router before you configure other IPv6 multicast features on the Router.

[Enabling IPv6 PIM-SM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2188b.html)

To enable a Router interface to establish IPv6 PIM neighbor relationships with other Routers, enable IPv6 PIM-SM.

[Setting an SSM Group Address Range](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2024.html)

The group address range in the Protocol Independent Multicast-Source-Specific Multicast (PIM-SSM) model is different from that in the PIM-SM model. If a multicast group that a user wants to join is within the SSM group address range, the PIM-SSM model is used to forward packets. If a multicast group that a user wants to join is beyond the SSM group address range, the PIM-SM model is used to forward packets. In PIM-SSM model, the default group address range is FF3x::/32. The SSM group address range can be changed as needed.

[(Optional) Limiting the Range of Multicast Source Addresses](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2189b.html)

You can configure multicast source addresses-based filtering policies by creating IPv6 ACLs. Then, an IPv6 PIM Router forwards only the multicast packets whose source address or source/group addresses match the IPv6 ACLs.

[(Optional) Configuring a Limit on the Number of PIM Entries](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2284_1.html)

IPv6 PIM-SSM allows you to limit the number of (S, G) entries. After a specified limit is reached, new (S, G) entries cannot be created.

[Verifying the IPv6 PIM-SSM Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2025.html)

After configuring IPv6 Protocol Independent Multicast-Source-Specific Multicast (PIM-SSM), verify PIM interfaces, PIM neighbors, and PIM routing tables by using related commands.