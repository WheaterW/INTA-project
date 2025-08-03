Understanding IPv6 NDP Vlink Direct Route Advertisement
=======================================================

Understanding IPv6 NDP Vlink Direct Route Advertisement

#### Purpose

By default, a device does not generate IPv6 Neighbor Discovery Protocol (NDP) Vlink direct routes in VLAN networking, and packets are forwarded through logical interfaces. However, direct routes of VLAN users are required in some scenarios. For example, a device needs to apply a unique export policy for each VLAN user to direct traffic of remote devices. In this scenario, Vlink direct routes need to be added to the routing table of a dynamic routing protocol and then advertised to remote devices.


#### Related Concepts

IPv6 NDP Vlink direct routes carry information about physical interfaces of VLAN users. These physical interface information is learned using NDP.


#### Implementation

In [Figure 1](#EN-US_CONCEPT_0000001130622778__fig_dc_vrp_ip-route_feature_003201), DeviceD is connected to DeviceA, DeviceB, and DeviceC through logical interfaces. DeviceE needs to communicate with DeviceB, but not with DeviceA or DeviceC. In this scenario, Vlink direct route advertisement must be enabled on DeviceD. DeviceD obtains IPv6 addresses of physical interfaces of DeviceA, DeviceB, and DeviceC, uses a route-policy to filter out network segment routes and routes destined for DeviceA and DeviceC, and advertises the route destined only for DeviceB to DeviceE.

**Figure 1** Vlink direct route advertisement  
![](figure/en-us_image_0000001176662327.png)

#### Application Scenario

Vlink direct route advertisement is applicable to networks on which a device needs to generate Vlink direct routes carrying information about physical interfaces of VLAN users, add the routes to the routing table of a dynamic routing protocol, and then advertise the routes to remote ends.


#### Benefits

After the advertisement of Vlink direct routes is enabled, the generated Vlink direct routes can be imported and advertised by a dynamic routing protocol (an IGP or BGP). Before routes are advertised, you can use different export route-policies for these direct routes to implement precise route control.