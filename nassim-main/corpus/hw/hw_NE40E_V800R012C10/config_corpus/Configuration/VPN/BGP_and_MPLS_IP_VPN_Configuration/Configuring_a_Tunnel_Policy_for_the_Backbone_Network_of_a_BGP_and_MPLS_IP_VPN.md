Configuring a Tunnel Policy for the Backbone Network of a BGP/MPLS IP VPN
=========================================================================

A tunnel policy applied to a VPN can specify the sequence
in which tunnels are selected for the VPN and enable load balancing
among tunnels.

#### Usage Scenario

By default, the system selects
a tunnel in the order of LSPs, MPLS TE tunnels, and Local\_IfNet for
VPN services, and does not perform load balancing. To configure load
balancing or change the selection sequence of tunnels, configure a
tunnel policy and apply it to the VPN.

At present, the NE40E supports the following types of tunnel policies:

* Tunnel type prioritizing policy: The sequence in which tunnels
  are selected or the number of tunnels participating in load balancing
  can be specified.
* Tunnel binding policy: A TE tunnel is bound to a specified
  destination IP address. This allows the VPN traffic destined for that
  destination address to be transmitted over the TE tunnel.

For details about tunnel policy configurations, see [VPN Tunnel Management
Configuration](dc_vrp_tnlm_cfg_0001.html).


#### Pre-configuration Tasks

Before configuring
a tunnel policy for the backbone network of a BGP/MPLS IP VPN, complete
the following tasks:

* Configure a basic BGP/MPLS IP VPN.
* Set up a tunnel of the type specified in the tunnel policy.


[Configuring a Tunnel Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2008.html)

A tunnel policy can determine the sequence in which tunnels are selected or bind a TE tunnel to a specified destination IP address.

[Applying a Tunnel Policy to a VPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2009.html)

This section describes how to apply a tunnel policy to a VPN to change the tunnel used to carry VPN services or the sequence in which tunnels are selected for VPN services.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2010.html)

After configuring a tunnel policy for the backbone network of a BGP/MPLS IP VPN, check the name of and configurations of the tunnel policy.