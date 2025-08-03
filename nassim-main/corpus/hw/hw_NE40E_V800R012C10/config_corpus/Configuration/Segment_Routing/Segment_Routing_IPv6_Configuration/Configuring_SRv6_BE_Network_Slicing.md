Configuring SRv6 BE Network Slicing
===================================

SRv6 BE network slicing enables a physical network to meet the differentiated requirements of various services.

#### Prerequisites

Before configuring SRv6 BE network slicing, complete the following task:

* Configure an IGP to implement network layer connectivity.

#### Context

Network slicing divides a physical network into multiple virtual networks that contain specific network functions and consist of customized network topologies and network resources. This meets the service function requirements of different network slice tenants and provides SLA assurance.

Before planning network slices, you need to create network slice instances and allocate slice IDs. A physical network is divided into multiple network slices by dividing interface forwarding resources.

On the network shown in [Figure 1](#EN-US_TASK_0000001163448571__fig8274193314262), network slice instances are created on P1 and P3, network slice interfaces are planned and bound to the network slice instances, and forwarding resources such as bandwidth are reserved.

**Figure 1** Interface-based network slice planning  
![](figure/en-us_image_0000001116448748.png)

In SRv6 BE network slicing scenarios, slice IDs are essential for connecting the control and forwarding planes, as shown in [Figure 2](#EN-US_TASK_0000001163448571__fig14542316102912).

**Figure 2** Connecting the control and forwarding planes through slice IDs  
![](figure/en-us_image_0000001116288840.png)


[Configuring Network Slice Instances](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0249a.html)

Configuring network slice instances is the first step for implementing network slicing. Interfaces can be added to network slices only after network slice instances are configured.

[Configuring Network Slice Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0250a.html)

You can configure network slice interfaces and specify the network slice instances to which they belong.

[Configuring a BGP Extended Community](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0113a.html)

This section describes how to add a BGP extended community, that is, the color extended community, to routes through a route-policy, enabling the routes to perform SRv6 recursion based on the color value.

[Configuring SRv6 BE Services](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0261.html)

After SRv6 BE services are configured, they can be forwarded based on network slices.

[Configuring Route Forwarding Based on Network Slices](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0258.html)

This section describes how to associate network slice services with forwarding resources through slice IDs.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0259.html)

After configuring SRv6 BE network slicing, you can verify the configuration.