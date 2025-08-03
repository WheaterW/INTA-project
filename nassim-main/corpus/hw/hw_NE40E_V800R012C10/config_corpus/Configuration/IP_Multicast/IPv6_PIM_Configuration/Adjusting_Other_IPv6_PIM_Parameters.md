Adjusting Other IPv6 PIM Parameters
===================================

You can adjust neighbor parameters, DR parameters, and forwarding parameters based on actual networking situations.

#### Usage Scenario

A Router can work normally with default control parameter configurations. If the default configurations do not fit your requirements, you can reconfigure the parameters, including neighbor parameters, Designated router (DR) parameters, and forwarding parameters.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If there is no special requirement, default parameter values are recommended.



#### Pre-configuration Tasks

Before adjusting other IPv6 PIM parameters, complete the following tasks:

* Configure an IPv6 unicast routing protocol to ensure that IPv6 unicast routes are reachable.
* [Configure IPv6 PIM-SM](dc_vrp_multicast_cfg_2005.html) or [configure IPv6 PIM-SSM](dc_vrp_multicast_cfg_2023.html).


[Adjusting the Lifetime of a Source](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2116.html)

A multicast device starts a timer for each (S, G) entry. If the multicast device does not receive any multicast packets from a multicast source within the specified lifetime of the multicast source, the multicast device considers that the (S, G) entry invalid, and the multicast source stops sending multicast data to the multicast group.

[Specifying the Source Address for Sending Register Messages (IPv6)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2209.html)

Specify the source address for sending Register messages on all devices that may become source's Designated routers (DRs). In this manner, registration errors will not occur due to repeated IP addresses on the network or filtered IPv6 addresses.

[Disabling IPv6 PIM Join/Prune Message Packaging](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2207.html)

Sending IPv6 Protocol Independent Multicast (PIM) Join/Prune messages in a package increases the rate at which the IPv6 PIM Join/Prune messages are sent.

[Adjusting Neighbor Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2027.html)

Devices establish neighbor relationships by exchanging Hello messages. PIM neighbor parameters include the interval for sending Hello messages, neighbor holdtime, whether to deny Hello messages without the Generation ID option, and neighbor filtering policy.

[Adjusting DR Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2028.html)

A source's Designated router (DR) is responsible for sending Register messages to a Rendezvous Point (RP), and a receiver's DR is responsible for sending Join messages to an RP. Devices elect a DR by exchanging Hello messages. The device with the highest priority wins the election. In the case of the same priority, the device with the largest IP address wins the election

[Adjusting Forwarding Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2029.html)

Parameters associated with PIM forwarding include the interval for sending Join/Prune messages, holdtime carried by a Join/Prune message, policy for filtering Join/Prune messages, and lan-delay and override-interval carried by a Hello message.

[Enabling a QinQ/dot1q VLAN Tag Termination Sub-Interface to Process IPv6 PIM Messages and Generate Multicast Forwarding Entries](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2286.html)

If a QinQ/dot1q VLAN tag termination sub-interface of a local device is connected to a remote device, you can enable the sub-interface to process IPv6 PIM messages and generate multicast forwarding entries so that the single-tagged IPv6 PIM messages received from the remote device can be processed and multicast forwarding entries are generated.

[Adjusting Assert Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2030.html)

The Router that fails in an election prohibits its downstream interface from forwarding multicast data in the period during which the Router retains the Assert state. After this period expires, the Router restores the forwarding capability of its downstream interface.

[Configuring the Alarm Function for the Sharp Decrease in the Number of Multicast (S, G) Entries](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_3171.html)



[Verifying the Configuration of Other IPv6 PIM Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2031.html)

After adjusting PIM neighbor parameters, Designated router (DR) parameters, forwarding parameters, or Assert parameters, verify information about PIM interfaces, PIM neighbors, PIM routing tables, and statistics about PIM control messages.