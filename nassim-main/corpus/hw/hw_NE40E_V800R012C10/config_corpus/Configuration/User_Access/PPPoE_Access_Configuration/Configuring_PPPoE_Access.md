Configuring PPPoE Access
========================

Configuring PPPoE access allows access control and accounting for hosts.

#### Usage Scenario

As network data services are developing rapidly, broadband users are increasing explosively. Carriers need an access device that can provide access services for multiple remote hosts and also provide user access control and accounting. Ethernet is the most economical technology for connecting multiple hosts to access devices. PPP provides well-developed user access control and accounting, but it cannot be applied to Ethernet. To address this issue, PPPoE has been developed. PPPoE is a link layer protocol that transmits PPP datagrams through PPP sessions established over point-to-point connections on Ethernet networks. As a supplement to PPP, PPPoE allows a remote access device to provide access services for hosts on Ethernet networks and to implement user access control and accounting. With these features, PPPoE is widely acknowledged among broadband access carriers, and therefore widely applied.


#### Pre-configuration Tasks

Before configuring PPPoE access, complete the following tasks:

* Configure AAA schemes.
* Configure a server template.
* Configure a local or remote IPv4 address pool.
* Configure a domain.
* Configure IP routing.


[Configuring a VT](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pppoe_cfg_0005.html)

Layer 2 protocols cannot directly communicate with each other. As such, you need to create a virtual template (VT) before configuring PPPoE access.

[Binding a VT to an Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pppoe_cfg_0007.html)

Bind a VT to an interface so that data on the interface can be transmitted based on parameters defined in the VT.

[(Optional) Configuring PPPoE Server Parameters](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pppoe_cfg_0020.html)

PPPoE server parameters can be configured as needed for negotiation between a PPPoE server and client.

[Binding a User VLAN to a Sub-interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pppox_cfg_0139.html)

To restrict broadcast packets on a LAN and enhance LAN security or create virtual groups, configure VLANs. VLANs apply only to Ethernet sub-interfaces.

[Configuring a BAS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pppox_cfg_0207.html)

If an interface is used for broadband access, you must configure it as a BAS interface. Before PPPoE users use a BAS interface to access a network, you must specify the access type as Layer 2 subscriber access.

[(Optional) Configuring Access Control on a BAS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pppox_cfg_0007a.html)

This section describes how to configure a BAS interface to filter access users so that only specified users are allowed to access the Router.

[(Optional) Configuring Refined IPv4 Route Advertisement](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pppox_cfg_0001.html)

Refined IPv4 route advertisement can classify routes and advertise them to different networks.

[(Optional) Configuring PPP User Access Limitations](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pppoe_cfg_0008.html)

To prevent unauthorized users from initiating a brute force attack to crack the password of an authorized user or the number of access users, configure the maximum number of users allowed to go online through a board or MAC address.

[(Optional) Enabling URPF for PPP Users](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pppox_cfg_0002.html)

Enabling URPF for PPP users prevents source address spoofing attacks.

[(Optional) Configuring the PPP Magic Number Check Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pppox_cfg_0285.html)

You can configure the PPP magic number check function to check whether a PPPoE user stays online after the user logs in.

[(Optional) Configuring Flexible Access to VPNs](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipox_cfg_0022_copy.html)

Service priorities can be identified based on 802.1p values of service packets and then transmitted to corresponding VPNs.

[(Optional) Enabling BGP Route Forwarding Between a CPE and BRAS for PPPoE Users](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_bras_0019.html)



[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pppoe_cfg_0009.html)

After configuring the PPPoE access service, check the PPPoE access configurations.