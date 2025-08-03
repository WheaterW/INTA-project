Configuring VPN GR Helper (IPv6)
================================

In the process of master/slave control board switchover or the system upgrade, you can configure VPN Graceful Restart (GR) Helper to ensure that VPN traffic is not interrupted on the PE, CE, or P. The NE40E supports only the GR Helper.

#### Usage Scenario

The VPN GR is enabled for the BGP/MPLS IPv6 VPN that needs the GR capability. Configuring VPN GR on the Router that undertakes the VPN service can ensure that Router keeps forwarding when the Router performs the mater/slave main control board switchover and the VPN traffic is not broken.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The GR capability cannot ensure that the traffic is not broken if the neighboring Router performs the mater/slave main control board switchover at the same time.

When configuring VPN GR, you must configure IGP GR, BGP GR, and MPLS LDP GR on the PE, configure IGP GR and MPLS LDP GR on the P, and configure IGP GR or BGP GR on the CE. If more than one domain is traversed, you must configure the IGP GR, BGP GR and MPLS LDP GR on the ASBR.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The NE40E supports only the GR Helper.



#### Pre-configuration Tasks

Before configuring VPN GR, complete the following tasks:

* Establish the VPN environment and configuring the VPN.
* Configure common IGP GR (such as IS-IS GR or OSPF GR), BGP GR and MPLS LDP GR on PEs and Ps in all related backbone networks to ensure that the backbone network has the GR capability.


[Configuring IGP GR Helper on the Backbone Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2075.html)

You can configure IGP GR Helper based on the specific IGP running on the backbone network.

[Configuring MPLS GR Helper on the Backbone Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2076.html)

In the process of master/slave control board switchover or the system upgrade, you can configure MPLS GR Helper to ensure normal MPLS traffic forwarding. If LDP LSPs are configured on the backbone network, you can configure MPLS LDP GR Helper; if RSVP-TE tunnels are configured on the backbone network, you can configure MPLS RSVP GR Helper; if other types of tunnels are configured on the backbone network, you do not need to perform the operation.

[Configuring GR Helper of the Routing Protocol Between PEs and CEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2077.html)

You can configure GR Helper of a routing protocol according to the specific routing protocol running between the CE and the PE.

[Configuring BGP GR Helper for MP-BGP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2078.html)

When MP-BGP restarts, the peer relationship is re-established and traffic forwarding is interrupted. If BGP GR Helper is enabled, traffic interruption can be prevented.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2079.html)

After configuring VPN GR Helper, you can check status information about IGP GR Helper, MPLS GR Helper, and BGP GR Helper.