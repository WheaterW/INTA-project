Configuring 802.1X Access Services
==================================

Before configuring 802.1X access services, familiarize
yourself with the usage scenario, complete the pre-configuration tasks,
and obtain the data required for the configuration.

#### Usage Scenario

To prevent unauthorized users or devices from gaining access to
a network and ensure network security, you can configure 802.1X access
services to allow only authorized users to access the network.


#### Pre-configuration Tasks

* Configure link-layer protocol parameters for interfaces to go
  Up at the link layer.
* Configure a routing protocol to implement IP connectivity of the
  network.


[Creating a Dot1x Template](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_8021x_cfg_0005.html)

When 802.1X authentication is used, an authentication server and 802.1X client perform authentication negotiation based on parameters defined in a dot1x template.

[Binding a 802.1X Template to a Domain](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_8021x_cfg_0006.html)

When 802.1X authentication is used for users in a domain, authentication negotiation is performed based on parameters defined in a dot1x template.

[(Optional) Binding a Sub-interface to a VLAN](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_8021x_cfg_0007.html)

When restrictions on broadcast packets are required in a LAN to enhance the LAN security or to set up virtual working groups, VLANs must be configured. VLANs can be used only on Ethernet sub-interfaces.

[Configuring a BAS interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_8021x_cfg_0008.html)

When an interface is used for broadband access, you need to configure it as a BAS interface and set the access type and relevant attributes for this interface.

[Verifying the 802.1X Access Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_8021x_cfg_0009.html)

After 802.1X access services are configured, check the configurations.