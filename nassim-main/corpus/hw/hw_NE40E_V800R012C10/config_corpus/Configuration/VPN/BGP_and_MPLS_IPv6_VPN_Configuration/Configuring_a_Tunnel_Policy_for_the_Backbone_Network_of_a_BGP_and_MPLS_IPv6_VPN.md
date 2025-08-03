Configuring a Tunnel Policy for the Backbone Network of a BGP/MPLS IPv6 VPN
===========================================================================

A tunnel policy applied to an IPv6 VPN can specify which tunnels are selected for the VPN and enable load balancing among tunnels.

#### Usage Scenario

By default, the system selects a tunnel in the order of LSPs, CR-LSPs, and local IFNET tunnels for IPv6 VPN services, and does not perform load balancing. To configure load balancing or change the selection sequence of tunnels, configure a tunnel policy and apply it to the IPv6 VPN.

At present, the NE40E supports the following types of tunnel policies:

* Select-sequence: Using this policy, you can specify the sequence in which tunnels are selected or the number of tunnels participating in load balancing.
* Tunnel binding: A TE tunnel is bound to a specified destination IP address. This allows the VPN traffic destined for that destination address to be transmitted over the TE tunnel.

For details about tunnel policy configurations, see [VPN Tunnel Management Configuration](dc_vrp_tnlm_cfg_0001.html).


#### Pre-configuration Tasks

Before configuring a tunnel policy for the backbone network of a BGP/MPLS IPv6 VPN, complete the following tasks:

* Configure a basic BGP/MPLS IPv6 VPN.
* Set up a tunnel of the type specified in the tunnel policy.


[Configuring a Tunnel Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2020.html)

A tunnel policy can determine the sequence in which tunnels are selected or bind a TE tunnel to a specified destination IP address.

[Applying a Tunnel Policy to an IPv6 VPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2021.html)

This section describes how to apply a tunnel policy to an IPv6 VPN to change the tunnel used to carry VPN services or the tunnel selection sequence for VPN services.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2022.html)

Check the name of the tunnel policy applied to a VPN and the configurations of the tunnel policy.