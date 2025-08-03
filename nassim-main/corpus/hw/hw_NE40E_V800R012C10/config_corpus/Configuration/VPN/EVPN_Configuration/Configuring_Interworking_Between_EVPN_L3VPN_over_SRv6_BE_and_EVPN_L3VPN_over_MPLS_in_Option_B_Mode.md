Configuring Interworking Between EVPN L3VPN over SRv6 BE and EVPN L3VPN over MPLS in Option B Mode
==================================================================================================

During network evolution, EVPN L3VPN over SRv6 BE and EVPN L3VPN over MPLS may coexist. To allow these two types of networks to communicate, perform this task.

#### Usage Scenario

EVPN L3VPN over BE and EVPN L3VPN over SRv6 can communicate in Option B mode.

**Figure 1** Interworking between EVPN L3VPN over SRv6 BE and EVPN L3VPN over MPLS  
![](figure/en-us_image_0000001271919105.png)

#### Pre-configuration Tasks

Before configuring interworking between EVPN L3VPN over SRv6 BE and EVPN L3VPN over MPLS in Option B mode, complete the following tasks:

* Configure basic MPLS functions on PE2 and the ASBR.
* Configure an IGP on PE1, PE2, and the ASBR to ensure route reachability.

* [Configure EVPN L3VPN over IS-IS SRv6 BE](dc_vrp_evpn_cfg_0152_copy.html) on the network where PE1 and the ASBR reside.
* [Configure EVPN L3VPN over MPLS](dc_vrp_evpn_cfg_0038.html) on the network where PE2 and the ASBR reside.


[Configuring Interworking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0217.html)

After enabling interworking between EVPN L3VPN over SRv6 BE and EVPN L3VPN over MPLS in Option B mode in the EVPN address family, configure SID application on a per-route or per-next-hop basis so that different types of tunnels can communicate with each other.

[Configuring a Tunnel Selector](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0218.html)

EVPN public network routes recurse to IP tunnels based on next hops by default. To enable EVPN public network routes to recurse to SRv6 BE tunnels based on next hops, deploy a tunnel selector for route matching.

[(Optional) Enabling ECMP or FRR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0219.html)



[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0220.html)

After configuring interworking between EVPN L3VPN over SRv6 BE and EVPN L3VPN over MPLS in Option B mode, check information about EVPN routes on PEs or ASBRs and the status of all BGP peer relationships.