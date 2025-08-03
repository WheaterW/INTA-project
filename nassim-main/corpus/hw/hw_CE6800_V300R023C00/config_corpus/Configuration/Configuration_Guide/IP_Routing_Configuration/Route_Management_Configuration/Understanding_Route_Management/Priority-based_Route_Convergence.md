Priority-based Route Convergence
================================

Priority-based Route Convergence

#### Definition

To improve network reliability, priority-based route convergence is essential. It provides faster route convergence for key services. In priority-based convergence, different convergence priorities are set for routes on a device, and the device converges routes based on priorities at a specified scheduling ratio to ensure uninterrupted service forwarding.


#### Purpose

With the network convergence, requirements on service differentiation increase. Carriers require that routes for key services, such as voice over IP (VoIP) and video conferencing services, converge faster than those for common services. In this case, route convergence needs to be performed based on convergence priorities to improve network reliability.


#### Route Convergence Priority

Route convergence priorities are critical, high, medium, and low. Critical routes have the highest convergence priority, and low routes have the lowest convergence priority. [Table 1](#EN-US_CONCEPT_0000001176662311__tab_dc_vrp_ip-route_feature_001001) lists the default convergence priorities of public network routes. You can set convergence priorities for routes as needed for a specific topology.

**Table 1** Default convergence priorities of public network routes
| Routing Protocol or Route Type | Convergence Priority |
| --- | --- |
| Direct | Critical |
| Static | Medium |
| OSPF and IS-IS host routes with 32-bit masks | Medium |
| OSPF (except 32-bit host routes) | Low |
| IS-IS (except 32-bit host routes) | Low |
| RIP | Low |
| BGP | Low |


![](../public_sys-resources/note_3.0-en-us.png) 

For VPN routes, the convergence priorities of OSPF and IS-IS host routes with 32-bit masks are medium, and those of the other routes are low.



#### Typical Application

An IGP runs on the network shown in [Figure 1](#EN-US_CONCEPT_0000001176662311__fig_dc_vrp_ip-route_feature_001001). DeviceA functions as the receiver, and DeviceB is connected to a server with IP address 10.10.10.10/32. The route to the server must be converged faster than other routes, for example, a route to 10.12.10.0/24. You can set a higher convergence priority for the route to 10.10.10.10/32 than that for the route to 10.12.10.0/24. In this case, the route to the server 10.10.10.10/32 is converged first, which ensures the proper transmission of key services.

**Figure 1** Network diagram of priority-based route convergence  
![](figure/en-us_image_0000001176662329.png)