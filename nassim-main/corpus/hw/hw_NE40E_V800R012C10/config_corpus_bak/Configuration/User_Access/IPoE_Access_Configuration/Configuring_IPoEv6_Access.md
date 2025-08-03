Configuring IPoEv6 Access
=========================

In IPoEv6 access, users can access the Internet by sending packets, without the need to install any client dial-up software for dialing in.

#### Context

IPoEv6 access is an access mode in which users access the NE40E by sending DHCPv6 packets, ND packets, or IPv6 packets.

IPoEv6 access can be classified into common IPoEv6 access, IPoEoVLANv6 access, and IPoEoQv6 access based on different protocol stacks. In IPoEv6 access mode, users can directly access the Internet using web browsers, without having to install client dial-up software on their PCs.

The service models of different carriers may differ, and the operating modes of home gateways may also differ on a broadband access network. A home gateway may operate in bridging mode, numbered routing mode, or unnumbered routing mode.


#### Pre-configuration Tasks

Before configuring IPoEv6 access, complete the following tasks:

* Load BRAS license files (For details, see the *HUAWEI NE40E-M2 seriesUniversal Service RouterConfiguration Guide-System Management*.)
* [Configuring AAA Schemes](dc_ne_aaa_cfg_0515.html) to configure authentication, authorization, and accounting schemes
* [Configuring a Device as a RADIUS Client](dc_ne_aaa_cfg_0600.html) , based on the protocol used by the AAA schemes
* [Configuring AAA Schemes for a Domain](dc_ne_aaa_cfg_0114.html) to bind authentication, authorization, and accounting schemes to the user domain
* [Configuring Servers for a Domain](dc_ne_aaa_cfg_0115.html) to bind a RADIUS or HWTACACS server to the user domain
* Enable IPv6 on the interfaces and configure IPv6 addresses (link-local addresses for Layer 2 access) on the interfaces

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If the link-local address is deleted or IPv6 is disabled on an interface or globally, the IPv6 protocol on the BAS interface goes down, and IPv4/IPv6 dual-stack users who access the BAS interface are logged out.



[Configuring an Authentication Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipoxv6_cfg_0007.html)

This section describes several authentication modes. Configure an authentication mode based on networking requirements.

[Configuring an Address Assignment Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipoxv6_cfg_0008.html)

The address assignment modes supported by the NE40E include NDRA, DHCPv6 (IA\_NA), DHCPv6 (IA\_PD), DHCPv6 (IA\_NA)+DHCPv6 (IA\_PD), and NDRA+DHCPv6 (IA\_PD). Configure an address assignment mode based on networking requirements.

[Binding a Sub-interface to a VLAN](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipox_cfg_0021b.html)

The NE40E processes tagged user packets received from different types of users in different manners to ensure proper packet forwarding.

[Configuring a BAS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipox_cfg_0043b.html)

When an interface is used for broadband access, you need to configure it as a BAS interface, and then specify the user access type and attributes for the interface.

[(Optional) Enabling One-to-Many Mapping Between One MAC Address and Many Sessions](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipoxv6_cfg_0066.html)



[(Optional) Configuring a Device to Send Reconfigure Messages to DHCPv6 Clients](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipoxv6_cfg_0068.html)



[Verifying the IPoEv6 Access Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipoxv6_cfg_0011.html)

After configuring IPoEv6 access, you can view IPoEv6 access configurations.