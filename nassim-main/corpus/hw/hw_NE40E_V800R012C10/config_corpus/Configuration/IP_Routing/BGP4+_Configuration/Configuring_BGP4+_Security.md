Configuring BGP4+ Security
==========================

To improve BGP4+ network security, you can configure BGP4+ authentication and GTSM on the BGP network.

#### Usage Scenario

You can configure the following functions to improve BGP4+ network security:

For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.

* MD5 authentication
  
  BGP4+ uses TCP as the transport protocol and considers a packet valid if the source address, destination address, source port, destination port, and TCP sequence number of the packet are correct. However, most parameters in a packet are easily accessible to attackers. To protect BGP4+ against attacks, configure MD5 authentication for TCP connections established between BGP4+ peers.
  
  To prevent the MD5 password set on a BGP4+ peer from being decrypted, update the MD5 password periodically.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The MD5 algorithm is not recommended if high security is required.
* Keychain authentication
  
  A keychain consists of multiple authentication keys, each of which contains an ID and a password. Each key in a keychain has a lifecycle, and keys are dynamically selected based on the lifecycle of each key. After a keychain with the same rules is configured on the two ends of a BGP4+ connection, the keychains can dynamically select authentication keys to enhance BGP4+ attack defense.
* TCP-AO authentication
  
  The TCP authentication option (TCP-AO) is used to authenticate received and to-be sent packets during TCP session establishment and data exchange. It supports packet integrity check to prevent TCP replay attacks. TCP-AO authentication improves the security of the TCP connection between BGP peers and is applicable to the network that requires high security.
* BGP4+ GTSM
  
  The GTSM mechanism protects the Router by checking whether the TTL value in an IP packet header is within a pre-defined range to enhance the system security.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  GTSM supports only unicast addresses. Therefore, configure GTSM on all the Routers configured with routing protocols.
* BGP4+ RPKI
  
  Resource Public Key Infrastructure (RPKI) improves BGP4+ security by validating the origin ASs of BGP4+ routes.

#### Pre-configuration Tasks

Before configuring BGP4+ security, [configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).


[Configuring BGP4+ Authentication](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0055.html)

BGP4+ authentication can be configured to enhance security of BGP networks.

[Configuring BGP4+ GTSM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0082.html)

To apply BGP4+ GTSM, you need to configure GTSM on both ends of the corresponding BGP4+ peer relationship.

[Configuring ROA](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_30991.html)

Resource Public Key Infrastructure (RPKI) can be configured to validate the origin of BGP4+ routes to ensure BGP4+ security. Route Origin Authorization (ROA) uses RPKI to validate and filter routes.

[Configuring ASPA](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_30993.html)

RPKIv2-based ASPA validation verifies the AS\_Path attribute of routes, ensuring BGP4+ security.

[Configuring Regional Validation](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_30992.html)

Resource Public Key Infrastructure (RPKI) regional validation or regional confederation validation ensures BGP4+ security by validating route advertisers.

[Configuring SSL/TLS Authentication for BGP4+](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_30995.html)

SSL/TLS authentication can be configured to encrypt BGP4+ messages, ensuring data transmission security.