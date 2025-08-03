Configuring an IPv4 over IPv6 Tunnel
====================================

An IPv4 over IPv6 tunnel functions as a permanent link that connects two IPv4 domains through the IPv6 backbone network. It is a fixed channel for regular and secure communication between border devices. An IPv4 over IPv6 tunnel is a point-to-point tunnel. The source and destination IPv6 addresses of the tunnel interfaces are manually specified, and must be unique on the same device.

#### Usage Scenario

To enable IPv4 networks to communicate with each other through an IPv6 network, configure an IPv4 over IPv6 tunnel on the devices where IPv4 networks border an IPv6 network.

On the network shown in [Figure 1](#EN-US_TASK_0172365242__fig_dc_vrp_4o6tnl_cfg_0003), an IPv4 over IPv6 tunnel can be established between two border devices to provide stable connection for isolated IPv4 networks or between a terminal and a border device to allow the terminal to access the remote IPv4 network. You can configure multiple IPv4 over IPv6 tunnels on a border device for communicating with multiple IPv6 networks.

**Figure 1** Networking diagram of an IPv4 over IPv6 tunnel  
![](images/fig_dc_vrp_4o6tnl_cfg_0003.png)  


#### Pre-configuration Tasks

Before configuring an IPv4 over IPv6 tunnel, connect interfaces and configure IPv6 addresses for the interfaces so that the route between the interfaces is reachable.


[Configuring a Source Interface for an IPv4 over IPv6 Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_4o6tnl_cfg_0003.html)

You can only specify a loopback interface as the source interface for an IPv4 over IPv6 tunnel interface and use it to communicate with other devices because a loopback interface stays in the Up state after being created.

[Configuring Tunnel Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_4o6tnl_cfg_0004.html)

This section describes how to create tunnel interfaces to implement communication between IPv4 networks over the tunnel established.

[Configuring IPv4 over IPv6 Tunnel Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_4o6tnl_cfg_0005.html)

Packets can be forwarded correctly only when Routers at two ends of a tunnel are configured with forwarding routes.

[(Optional) Configuring Other Parameters of an IPv4 over IPv6 Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_4o6tnl_cfg_0006.html)

This section describes how to configure an IPv6 packet header for an IPv4 packet so that the packet can be transmitted over an IPv4 over IPv6 tunnel.

[Verifying the Configuration of an IPv4 over IPv6 Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_4o6tnl_cfg_0007.html)

After configuring an IPv4 over IPv6 tunnel, you can check the status of the tunnel interfaces and routing information.