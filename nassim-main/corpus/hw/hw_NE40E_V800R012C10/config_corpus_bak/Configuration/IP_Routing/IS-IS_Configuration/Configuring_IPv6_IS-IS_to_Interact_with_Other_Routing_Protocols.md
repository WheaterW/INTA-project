Configuring IPv6 IS-IS to Interact with Other Routing Protocols
===============================================================

If other routing protocols are configured on an IS-IS network, configure IS-IS to interact with these protocols for communication between them.

#### Usage Scenario

If other routing protocols are configured on an IS-IS network, note the following issues:

* Priorities of IS-IS routes
  
  If multiple routes to the same destination are discovered by different routing protocols running on the same device, the route discovered by the protocol with the highest priority is selected. For example, if both OSPF and IS-IS are configured, the route discovered by OSPF is used because OSPF enjoys a higher priority than IS-IS by default.
  
  If you want the route discovered by IS-IS to be preferentially selected, configure a higher priority for the route.
* Communication between areas
  
  If other routing protocols are configured on an IS-IS network, configure IS-IS to interact with those routing protocols so that IS-IS areas can communicate with non-IS-IS areas.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The LSDBs of different IS-IS processes on a device are independent of each other. Therefore, each IS-IS process on the device considers routes of the other IS-IS processes as external routes.
  
  
  To ensure successful traffic forwarding, configure IS-IS to import external routes on a device (such as a Level-1-2 IS-IS router) where external routes are configured. Such configuration enables all devices in IS-IS areas to learn external routes, implementing refined control over traffic forwarding.
  
  To ensure successful forwarding of traffic destined for IS-IS areas, enable the other routing protocols to interact with IS-IS.


#### Pre-configuration Tasks

Before configuring IPv6 IS-IS to interact with other routing protocols, complete the following tasks:

* Configure the link layer protocol on interfaces.
* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic IPv6 IS-IS functions](dc_vrp_isis_cfg_1023.html).
* Configure basic functions of other routing protocols.


[Configuring a Preference Value for IPv6 IS-IS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1037.html)

If there are multiple types of routes to the same destination, you can set a preference for IS-IS to enable IS-IS routes to be preferentially selected.

[Configuring IPv6 IS-IS to Import External Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1038.html)

Configuring IS-IS to import external routes on a boundary device enables devices in the IS-IS domain to learn external routes and guide traffic forwarding.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1039.html)

After enabling IS-IS to import routes from other protocols, check the IS-IS and IP routing tables.