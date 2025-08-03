Configuring Route Reflection to Optimize the VPN Backbone Layer
===============================================================

Using an RR helps reduce the number of MP-IBGP connections
between PEs. The RR not only reduces the burden on PEs, but also facilitates
network maintenance and management.

#### Usage Scenario

If too many PEs reside on
the VPN backbone layer and these PEs need to establish MP-IBGP peer
relationships to exchange VPN routes, you can configure route reflection
to optimize the VPN backbone layer.

A BGP speaker does not advertise
the routes learned from an IBGP peer to other IBGP peers. To enable
a PE to advertise the routes of the VPN that the PE accesses to the
BGP VPNv4 peers in the same AS, the PE must establish IBGP peer relationships
with all peers to directly exchange VPN routing information. In other
words, MP-IBGP peers must be fully meshed. If there are n PEs (including
ASBRs) in an AS, n (n-1)/2 MP-IBGP peer relationships need to be established.
A large number of IBGP peers consume a great number of network resources.
After an RR is configured, each PE needs to set up an MP-IBGP peer
relationship with only the RR, that is, only n pairs of MP-IBGP peers
are required.


#### Pre-configuration Tasks

Before configuring
route reflection to optimize the VPN backbone layer, complete the
following tasks:

* Configure a routing protocol on the MPLS backbone network to
  ensure IP connectivity on the backbone network.
* Establish tunnels (LSPs or MPLS TE tunnels) between all the
  PEs.


[Configuring a Client PE to Establish an MP-IBGP Peer Relationship with an RR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0017.html)

You can configure a PE to establish an MP-IBGP peer relationship with an RR so that the PE can receive VPNv4 routes reflected by the RR.

[Configuring an RR to Establish MP-IBGP Peer Relationships with All Client PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0018.html)

You can configure an RR to establish MP-IBGP peer relationships with all its client PEs to reflect VPNv4 routes.

[Configuring Route Reflection for BGP VPNv4 Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0019.html)

The prerequisite for enabling BGP VPNv4 route reflection is that the RR has established MP-IBGP peer relationships with all client PEs.

[Verifying the Configuration of Route Reflection to Optimize the VPN Backbone Layer](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0020.html)

After configuring route reflection to optimize the VPN backbone layer, check BGP VPNv4 peer information and VPNv4 routing information on the RR or its client PEs.