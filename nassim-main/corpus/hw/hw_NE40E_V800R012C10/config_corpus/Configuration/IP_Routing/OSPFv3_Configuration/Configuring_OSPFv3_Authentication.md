Configuring OSPFv3 Authentication
=================================

Configuring OSPFv3 authentication enables a device to authenticate sent and received OSPFv3 packets, protecting the device against attacks through forged OSPFv3 packets.

#### Usage Scenario

OSPFv3 IPsec uses a complete set of IPsec mechanisms to authenticate sent and received OSPFv3 packets, protecting devices against forged OSPFv3 packets.

However, on some special networks, a mobile ad hoc network (MANET) for example, IPsec is difficult to deploy and maintain. To address this problem, Authentication Trailer for OSPFv3 can be used to implement authentication.

If Authentication Trailer for OSPFv3 is used, an authentication field is added to each OSPFv3 packet for encryption. When receiving an OSPFv3 packet from a remote device, the local device discards the packet if the authentication password carried in the packet is different from the local one, protecting the local device against potential attacks.


#### Pre-configuration Tasks

Before configuring OSPFv3 authentication, complete the following tasks:

* Enable IPv6.
* [Configure basic OSPFv3 functions](dc_vrp_ospfv3_cfg_2003.html).
* If keychain authentication needs to be used, [configure basic keychain functions](dc_vrp_keychain_cfg_0005.html).


[Configuring OSPFv3 IPsec](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2082.html)

OSPFv3 IPsec provides a set of IPsec mechanisms to authenticate sent and received OSPFv3 packets, protecting devices against invalid OSPFv3 packets.

[Configuring OSPFv3 Authentication Trailer](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2083.html)

Open Shortest Path First version 3 (OSPFv3) supports packet authentication, enabling OSPFv3 devices to receive only the OSPFv3 packets that are authenticated. If packets fail to be authenticated, OSPFv3 neighbor relationships cannot be established. This section describes how to configure an authentication mode.

[Configuring OSPFv3 Process Authentication](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2083_1.html)

OSPFv3 supports packet authentication, with which devices accept only the OSPFv3 packets that are authenticated. If OSPFv3 packets fail to be authenticated, OSPFv3 neighbor relationships cannot be established. Configuring OSPFv3 process authentication improves OSPFv3 network security.

[Configuring OSPFv3 Area Authentication](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2083_2.html)

OSPFv3 supports packet authentication, with which devices accept only the OSPFv3 packets that are authenticated. If OSPFv3 packets fail to be authenticated, OSPFv3 neighbor relationships cannot be established. Configuring OSPFv3 area authentication improves OSPFv3 network security.

[Configuring OSPFv3 Interface Authentication](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2083_3.html)

OSPFv3 supports packet authentication, with which devices accept only the OSPFv3 packets that are authenticated. If OSPFv3 packets fail to be authenticated, OSPFv3 neighbor relationships cannot be established. Configuring OSPFv3 interface authentication improves OSPFv3 network security.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2084.html)

After configuring OSPFv3 authentication, you can check the configurations.