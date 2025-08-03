Configuring a Policy for Processing MLD Message
===============================================

In this configuration task, you can configure a device to deny all the MLD packets without Router-Alert options, send MLD packets without Router-Alert options, and filter MLD packets based on source addresses.

#### Usage Scenario

Generally, a device sends a packet to the routing protocol layer for processing only if the destination IP address of the packet is the IP address of a local interface. The destination IP address of an MLD packet is usually a multicast address but not the address of an interface on a multicast device and thus the MLD packet may fail to be sent to the routing protocol layer for processing. Router-Alert options can address such a problem. MLD packets carrying Router-Alert options need to be sent to the routing protocol layer for processing.

To improve a device's security, you can configure a device to filter MLD packets based on source addresses. This filtering function is implemented by specifying source addresses in ACL rules, so the device permits an MLD packet only if the packet carries a source address that is specified as a valid source address in an ACL rule.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

For details about Router-Alert options, see relevant standards.



#### Pre-configuration Tasks

Before configuring a Policy for Processing MLD message, complete the following tasks:

* Configuring a unicast routing protocol to make devices routable
* [Configuring Basic MLD Functions](dc_vrp_multicast_cfg_2073.html)


[Configuring the Router to Deny MLD Messages Without the Router-Alert Option](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2084.html)

If user hosts do not want to receive MLD messages without the Router-Alert option, configure the Router directly connected to the user hosts to deny all MLD messages without the Router-Alert option.

[Configuring the Router to Send MLD Messages Without the Router-Alert Option](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2085.html)

If some MLD interfaces on the same network need to receive MLD messages without the Router-Alert option, configure the Router connected to the user network segment to send MLD messages without the Router-Alert option.

[Setting the Maximum Number of MLD Group Members That an Interface Can Maintain](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast-mld_cfg_2096.html)

This section describes how to configure an MLD entry limit on an interface to allow users who have joined multicast groups to enjoy smoother multicast services.

[Configuring Source Address-based MLD Message Filtering](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2225.html)

Source address-based MLD message filtering is a security policy used for filtering MLD message on the Router's interface connected to user hosts.

[Configuring Micro-Isolation CAR for MLD](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast-mld_cfg_2278.html)



[Verifying the Configuration of the Policy for Processing MLD Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2226.html)

After configuring the Policy for Processing MLD Packets, verify MLD configurations and running information on the interface to ensure normal running of MLD.