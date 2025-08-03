Configuring a GRE Tunnel
========================

GRE provides a mechanism of encapsulating packets of a protocol into packets of another protocol. This allows packets to be transmitted over heterogeneous networks. The channel for transmitting heterogeneous packets is called a tunnel.

#### Usage Scenario

A single network protocol (for example, IPv4) is generally used to transmit packets on the backbone network, whereas other protocols, such as IP, IPv6, and Internet Packet Exchange (IPX), are used to transmit packets on non-backbone networks. Because the backbone and non-backbone networks use different protocols, packets cannot be transmitted between the non-backbone networks over the backbone network. GRE resolves this issue by providing a mechanism of encapsulating packets of a protocol into packets of another protocol.


#### Pre-configuration Tasks

Before configuring a GRE tunnel, complete the following task:

* Configuring reachable routes between the source and destination interfaces


[Binding an Interface to GRE](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_gre_cfg_1002.html)

A GRE tunnel's source interface or the interface where the source address of a GRE tunnel resides must be bound to GRE. The GRE tunnel can use these interfaces to transmit GRE-encapsulated packets only after these interfaces are bound to GRE.

[Configuring Tunnel Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_gre_cfg_2004.html)

After creating a tunnel interface, you need to specify GRE as the encapsulation type and configure a source address or source interface and a destination address for the tunnel interface. To enable the tunnel to support dynamic routing protocols, you aso need to configure an IP address for the tunnel interface.

[Configuring a Route for a Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_gre_cfg_2005.html)

A route for a tunnel must be available on both the source and destination devices so that packets encapsulated with GRE can be forwarded correctly. A route passing through a tunnel interface can be either a static or dynamic route.

[(Optional) Configuring the TTL Processing Mode for GRE Tunnels](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_gre_cfg_1001.html)

This section describes how to configure GRE tunnels to process TTL in pipe or uniform mode.

[(Optional) Enabling the Keepalive Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_gre_cfg_2009.html)

The keepalive function of a GRE tunnel prevents a service module from selecting a GRE tunnel that is unreachable to the peer end, preventing data loss.

[(Optional) Configuring GRE Security Options](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_gre_cfg_2041.html)

Configuring GRE security options can improve GRE tunnel security.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_gre_cfg_2007.html)

After a GRE tunnel is set up, you can check the running status and routing information of the tunnel interface.