Improving BGP Security
======================

To improve BGP network security, you can configure BGP authentication, RPKI, and GTSM on the BGP network.

#### Usage Scenario

You can configure the following functions to improve BGP network security:

For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.

* MD5 authentication
  
  BGP uses TCP as the transport protocol and considers a packet valid if the source address, destination address, source port, destination port, and TCP sequence number of the packet are correct. However, most parameters in a packet are easily accessible to attackers. To protect BGP against attacks, configure MD5 authentication for TCP connections established between BGP peers.
  
  To prevent the MD5 password set on a BGP peer from being decrypted, update the MD5 password periodically.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The MD5 algorithm is not recommended if high security is required.
* Keychain authentication
  
  A keychain consists of multiple authentication keys, each of which contains an ID and a password. Each key has a lifecycle, and keys are dynamically selected based on the life cycle of each key. After a keychain with the same rules is configured on the two ends of a BGP connection, the keychains can dynamically select authentication keys to enhance BGP attack defense.
* BGP GTSM
  
  The GTSM mechanism protects the Router by checking whether the TTL value in an IP packet header is within a pre-defined range, which enhances the system security.
* BGP RPKI
  
  Resource Public Key Infrastructure (RPKI) improves BGP security by validating the origin ASs of BGP routes.
* SSL/TLS authentication
  
  Secure Sockets Layer (SSL) is a security protocol that protects data privacy on the Internet. Transport Layer Security (TLS) is a successor of SSL. TLS protects data integrity and privacy by preventing attackers from eavesdropping the data exchanged between a client and server. To ensure data transmission security on a network, SSL/TLS authentication can be enabled for BGP message encryption.
* TCP-AO authentication
  
  The TCP authentication option (TCP-AO) is used to authenticate received and to-be sent packets during TCP session establishment and data exchange. It supports packet integrity check to prevent TCP replay attacks. TCP-AO authentication improves the security of the TCP connection between BGP peers and is applicable to the network that requires high security.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

GTSM supports only unicast addresses. Therefore, configure GTSM on all the Routers configured with routing protocols.



#### Pre-configuration Tasks

Before configuring BGP security, complete the following tasks:

* [Configure basic BGP functions.](dc_vrp_bgp_cfg_3004.html)
* [Configure a keychain.](dc_vrp_keychain_cfg_0005.html)


[Configuring MD5 Authentication](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3063.html)

In MD5 authentication, a Message Digest 5 (MD5) authentication password is set for a TCP connection, and the MD5 authentication is performed by TCP. If authentication fails, no TCP connection will be established.

[Configuring Keychain Authentication](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3064.html)

After a keychain with the same rules is configured on the two ends of a BGP connection, the keychain can dynamically select the authentication keys to enhance BGP attack defense.

[Configuring TCP-AO Authentication](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_tcp-ao.html)

This section describes how to configure BGP TCP Authentication Option (TCP-AO) authentication to check the integrity of packets and prevent TCP replay attacks.

[Configuring BGP GTSM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3065.html)

To apply BGP GTSM, you need to configure GTSM on both ends of the corresponding BGP peer relationship.

[Configuring ROA](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_30991.html)

Resource Public Key Infrastructure (RPKI) can validate the origin of BGP routes, ensuring BGP security. Using RPKI, Route Origin Authorization (ROA) can validate and filter routes.

[Configuring ASPA](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_30993.html)

RPKIv2-based ASPA validation validates the AS\_Path attribute of routes, ensuring BGP security.

[Configuring Regional Validation](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_30992.html)

Resource Public Key Infrastructure (RPKI) regional validation or regional confederation validation ensures BGP security by validating route advertisers.

[Enabling SSL/TLS Authentication for BGP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_4055.html)

SSL/TLS authentication can be configured to encrypt BGP messages, ensuring data transmission security.