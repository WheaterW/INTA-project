Configuring IPoEv4 Access
=========================

In IPoE access, users can access the Internet by sending packets, without the need to install any client dialup software for dialing in.

#### Usage Scenario

IPoE access is an access authentication service. In IPoE access, a user accesses the Internet by using the Ethernet or asymmetric digital subscriber line (ADSL). The user is configured with a fixed IP address or is assigned an IP address through Dynamic Host Configuration Protocol (DHCP). The system then authenticates the user using web authentication, fast authentication, or binding authentication.

Depending on the networking, IPoE access can be classified into common IPoE access, IPoEoVLAN access, and IPoEoQ access.


#### Pre-configuration Tasks

Before configuring IPoE access, complete the following tasks:

* Configure Authorization, Authentication, and Accounting (AAA) schemes.
* Configure a server template.
* Configure an IPv4 address pool.
* Configure a domain.


[Binding a Sub-interface to a VLAN](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipox_cfg_0021.html)

The NE40E processes tagged user packets received from different types of users in different manners to ensure proper packet forwarding.

[Configuring a BAS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipox_cfg_0043.html)

When an interface is used for broadband access, you need to configure it as a BAS interface, and then specify the user access type and attributes for the interface.

[(Optional) Configuring Access Control on a BAS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipox_cfg_0007.html)

This section describes how to configure a BAS interface to filter access users so that only specified users are allowed to access the Router.

[(Optional) Enabling One-to-Many Mapping Between One MAC Address and Many Sessions](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipox_cfg_0012.html)



[(Optional) Configuring Gateway Unnumbered](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_bras_0014.html)



[(Optional) Configuring Flexible Access to VPNs](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipox_cfg_0022.html)

Service priorities can be identified based on 802.1p values of service packets and then transmitted to corresponding VPNs.

[(Optional) Configuring a Basic Protocol Stack for IPoE Dual-stack Users](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipox_cfg_0175_copy.html)

This section describes how to configure a basic protocol stack for IPoE dual-stack users so that the device allows user access from the other stack only after it detects that the users have been online from the basic protocol stack.

[(Optional) Configuring a Whitelist for Web Users Who Access the Network Using HTTPS](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipox_cfg_0176.html)

This section describes how to configure a whitelist for web users who access the network using HTTPS.

[(Optional) Enabling BGP Route Forwarding Between a CPE and a BRAS](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_bras_00199.html)



[(Optional) Configuring a BAS Interface to Send RIP Routes](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_bras_0129.html)



[Verifying the IPoE Access Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipox_cfg_0044.html)

After configuring IPoE access, you can view information about IPoE access.