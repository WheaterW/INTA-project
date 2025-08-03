Configuring Association Between Direct Routes and a VRRP Group
==============================================================

Association between direct routes and a Virtual Router Redundancy Protocol (VRRP) group ensures that both network-to-user traffic and user-to-network traffic that traverse the VRRP group travel along the same path, which facilitates network management and improves reliability.

#### Usage Scenario

On a live network, a VRRP group serves as a gateway for users (including common users and base stations) to access the network. User-to-network traffic traverses the master device in the VRRP group, while network-to-user traffic travels along a path that a dynamic routing protocol selects. Therefore, user-to-network traffic and network-to-user traffic may travel along different paths, which may block traffic if firewalls are attached to devices in the VRRP group, complicates traffic monitoring or statistics collection, and increases costs.

To address the preceding problems, you can associate direct routes with a VRRP group so that the VRRP group status affects route costs and thereby changes route selection results. This ensures that user-to-network and network-to-user traffic is transmitted along the same path.


#### Pre-configuration Tasks

Before associating direct routes with a VRRP group, complete the following tasks:

* Configure VRRP basic functions and create a VRRP group.
* Configure a dynamic routing protocol to ensure IP route reachability among nodes.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

With association between direct routes and a VRRP group, VRRP and RIP cannot be configured on the same interface. If VRRP and RIP are configured on the same interface, RIP cannot inherit the route costs from the imported direct routes. As a result, association between direct routes and a VRRP group is not implemented, and the RIP route selection result is affected.



[Associating Direct Routes with a VRRP Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ip-route_cfg_0030.html)

Associating direct routes with a VRRP group on a VRRP-enabled interface or a Loopback interface allows the interface to modify the cost of each direct route to the virtual IP network segment based on the VRRP status.

[Configuring a Dynamic Routing Protocol to Import Direct Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ip-route_cfg_0031.html)

After you associate direct routes with a Virtual Router Redundancy Protocol (VRRP) group, configure a dynamic routing protocol to import the direct routes so that the path selection by the dynamic routing protocol can be controlled.

[Verifying the Configuration of Association Between Direct Routes and a VRRP Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ip-route_cfg_0032.html)

After you associate direct routes with a Virtual Router Redundancy Protocol (VRRP) group, you can view information about the VRRP group and information in the routing table of the previous-hop device on the network side.