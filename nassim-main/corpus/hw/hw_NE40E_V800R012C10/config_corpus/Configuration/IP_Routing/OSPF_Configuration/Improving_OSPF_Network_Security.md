Improving OSPF Network Security
===============================

On a network demanding high security, you can configure OSPF authentication and GTSM to improve OSPF network security.

#### Usage Scenario

With the increase in attacks on TCP/IP networks and the defects in the TCP/IP protocol suite, network attacks have increasing impacts on the network security. Attacks on network devices may lead to network crash. Configuring OSPF authentication and GTSM can improve OSPF network security.

OSPF authentication encrypts OSPF packets by adding authentication information to IP headers of the OSPF packets to ensure network security. When receiving an OSPF packet from a remote device, the local device discards the packet if the authentication password carried in the packet is different from the local one, protecting the local device against potential attacks.

In terms of the packet type, the authentication is classified as follows:

* Area authentication: configured in the OSPF area view and applies to packets on all interfaces in the OSPF area.
* Interface authentication: configured in the interface view and applies to all packets on the interface.

#### Pre-configuration Tasks

Before improving OSPF network security, complete the following tasks:

* Configure a link layer protocol.
* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic OSPF functions](dc_vrp_ospf_cfg_0003.html).
* [Configure basic Keychain functions](dc_vrp_keychain_cfg_0005.html).


[Configuring Area Authentication](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0080.html)

OSPF supports packet authentication. With the authentication, only the packets that are authenticated are accepted; if packets fail to be authenticated, a neighbor relationship cannot be established. If area authentication is used, the authentication mode and password configurations on all the interfaces in the area must be identical.

[Configuring Interface Authentication](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0081.html)

Interface authentication takes effect between neighboring devices' interfaces on which an authentication mode and password are configured. Interface authentication takes precedence over area authentication. Interfaces on the same network segment must have the same authentication mode and password. Interfaces on different network segments can have different authentication modes and passwords.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0082.html)

After configuring OSPF functions to improve OSPF network security, check the configuration.