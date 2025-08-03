Configuring DSVPN
=================

Configure DSVPN to dynamically establish VPNs between branches and the HQ and between branches in the hub-spoke network model.

#### Usage Scenario

The HQ (hub) is connected to multiple branches (spoke) at different locations through the public network. To implement direct communication between branches and between the branches and the HQ, you need to deploy DSVPN on the hub-spoke network, implementing communication between branches and the HQ and between branches.


#### Pre-configuration Tasks

Before configuring static DSVPN, complete the following tasks:

Assign an IP address to each involved interface.


[Configuring mGRE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_cfg_dsvpn_0006.html)

Setting the tunnel interface type to mGRE allows multiple GRE tunnels to be established on the same tunnel interface, simplifying configuration.

[Configuring Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_cfg_dsvpn_0007.html)

DSVPN routes need to be configured appropriately to ensure the correct forwarding of mGRE-encapsulated packets.

[Configuring NHRP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_cfg_dsvpn_0008.html)

Configure the Next Hop Resolution Protocol (NHRP) so that spokes can obtain the peer IP address of each other by exchanging NHRP Resolution Request and Reply packets.

[(Optional) Configuring an IPsec Profile](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_cfg_dsvpn_0009.html)

Configure an IPsec profile to encrypt transmitted data to improve network security.

[Checking the DSVPN Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_cfg_dsvpn_0010.html)

After completing the configuration task, verify the DSVPN configuration.