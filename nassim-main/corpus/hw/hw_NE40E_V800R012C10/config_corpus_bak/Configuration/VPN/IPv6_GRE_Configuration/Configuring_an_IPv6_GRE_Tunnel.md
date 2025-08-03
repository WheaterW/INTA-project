Configuring an IPv6 GRE Tunnel
==============================

IPv6 Generic Routing Encapsulation (GRE) provides a mechanism
of encapsulating packets of a protocol into packets of another protocol.
This allows packets to be transmitted over heterogeneous networks.
The channel for transmitting heterogeneous packets is called a tunnel.

#### Usage Scenario

A single network protocol
is used to transmit packets on a backbone network, whereas other protocols
are used to transmit packets on non-backbone networks. Because the
backbone and non-backbone networks use different protocols, packets
cannot be transmitted between the non-backbone networks over the backbone
network. IPv6 GRE resolves this issue. IPv6 GRE provides a mechanism
of encapsulating packets of a protocol into packets of another protocol.

![](../../../../public_sys-resources/note_3.0-en-us.png) For an IPv6 GRE tunnel:

* The packet transmission protocol is IPv6.
* Only IPv4 and IPv6 packets can be encapsulated and routed currently.



#### Pre-configuration Tasks

Before configuring
an ordinary IPv6 GRE tunnel, configure reachable routes between the
source and destination interfaces.


[Configuring the Interface Bound to GRE](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_gre_cfg_1002_a.html)

A GRE tunnel's source interface or the interface where the source address of a GRE tunnel resides must be bound to GRE. The GRE tunnel can use these interfaces to transmit GRE-encapsulated packets only after these interfaces are bound to GRE.

[Configuring Tunnel Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_gre_cfg_2046.html)

After creating a tunnel interface, you need to specify IPv6 GRE as the encapsulation type and configure a source address and a destination address for the tunnel interface. To enable the tunnel to support dynamic routing protocols, you aso need to configure an IP address for the tunnel interface.

[Configuring Tunnel Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_gre_cfg_2047.html)

Routes for a tunnel must be available on both the source and destination devices so that packets encapsulated with GRE can be forwarded correctly. 

[Verifying the IPv6 GRE Tunnel Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_gre_cfg_2048.html)

After configuring an IPv6 GRE tunnel, you can check the status of the tunnel interface and routing information.