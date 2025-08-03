Adjusting Other PIM Parameters
==============================

You can adjust neighbor parameters, Designated router (DR) parameters, and forwarding parameters based on actual networking situations.

#### Usage Scenario

A Router can work normally with default control parameter configurations. If the default configurations do not fit your requirements, you can reconfigure the parameters, including neighbor parameters, DR parameters, and forwarding parameters.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If there is no special requirement, default parameter values are recommended.



#### Pre-configuration Tasks

Before adjusting other PIM parameters, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* [Configure PIM-SM](dc_vrp_multicast_cfg_0006.html) or [configure PIM-SSM](dc_vrp_multicast_cfg_0023.html).


[Adjusting the Lifetime of a Source](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0098.html)

A multicast device starts a timer for each (S, G) entry. If the multicast device does not receive any multicast packets from a multicast source within the specified lifetime of the multicast source, the multicast device considers that the (S, G) entry invalid, and the multicast source stops sending multicast data to the multicast group.

[Specifying the Source Address for Sending Register Messages](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2208.html)

Specify the source address for sending Register messages on all devices that may become source's Designated routers (DRs). In this manner, registration errors will not occur due to repeated IP addresses on the network or filtered IP addresses.

[Disabling Join/Prune Message Packaging](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2206.html)

Sending PIM Join/Prune messages in a package increases the transmission rate.

[Adjusting Neighbor Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0027.html)

Devices establish neighbor relationships by exchanging Hello messages. PIM neighbor parameters include the interval for sending Hello messages, timeout period of a neighbor relationship, whether to deny a Hello message carrying the Generation ID option, and policy for filtering neighbors.

[Adjusting DR Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0028.html)

A source's Designated router (DR) is responsible for sending Register messages to a Rendezvous Point (RP), and a receiver's DR is responsible for sending Join messages to an RP. The Routers elect a DR by exchanging Hello messages. The Router with the highest priority wins the election. If the Router have the same priority, the Router with the largest IP address wins the election.

[Configuring the Sticky DR Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_3159.html)

The sticky DR function keeps the role of the device that is elected as the DR unchanged.

[Adjusting Forwarding Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0029.html)

Parameters associated with PIM forwarding include the interval for sending Join/Prune messages, holdtime carried by a Join/Prune message, policy for filtering Join/Prune messages, and lan-delay and override-interval carried by a Hello message.

[Enabling a QinQ/dot1q VLAN Tag Termination Sub-Interface to Process PIM Messages and Generate Multicast Forwarding Entries](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0109.html)

If a QinQ/dot1q VLAN tag termination sub-interface of a local device is connected to a remote device, you can enable the sub-interface to process PIM messages and generate multicast forwarding entries so that the single-tagged PIM messages received from the remote device can be processed and multicast forwarding entries are generated.

[Adjusting Assert Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0030.html)

When multiple multicast data forwarders exist on a shared network segment, the Routers elect a unique forwarder through the Assert mechanism. The Router that fails in the election prevents its downstream interface from forwarding multicast data within the holdtime of the Assert state. After the holdtime of the Assert state expires, the downstream interface is allowed to forward multicast data.

[Configuring the Alarm Function for the Sharp Decrease in the Number of Multicast (S, G) Entries](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_3157.html)



[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0031.html)

After adjusting PIM neighbor parameters, Designated router (DR) parameters, forwarding parameters, or Assert parameters, verify information about PIM interfaces, PIM neighbors, PIM routing tables, and statistics about PIM control messages.